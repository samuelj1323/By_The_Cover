from flask import Flask, render_template
import base64
import requests
import datetime
from urllib.parse import urlencode
import json
import numpy as np
from pandas import*
app = Flask(__name__)


class spotify_api(object): 
        access_token = None
        access_token_exires = datetime.datetime.now()
        access_token_did_expire = True
        id = None
        secret = None
        token_url = 'https://accounts.spotify.com/api/token'

        def __init__(self, id, secret, *args, **kwargs): #constructor
                super().__init__(*args, **kwargs)
                self.id = id
                self.secret = secret

        def get_token_header(self): #formatting token header for auth api call
                id = self.id
                secret = self.secret

                if secret == None or id == None:
                        raise Exception("Neeed client id and client secret")
                
                creds = f'{id}:{secret}'
                creds_b64 = base64.b64encode(creds.encode()) #needs to be base 64 encoded for spotify api

                return {
                        'Authorization': f"Basic {creds_b64.decode()}"
                }

        def get_token_data(self): #formatting data for auth api call
                return {
                        'grant_type': 'client_credentials'
                }

        def do_auth(self): #will preform the authentication and return true if suceesfull, and false if failed
                token_url = self.token_url
                token_data = self.get_token_data()
                token_header = self.get_token_header()
                r = requests.post(token_url, data=token_data, headers=token_header)
                if r.status_code not in range(200, 299):
                        raise Exception("auth failed")
                token_response = r.json()
                now = datetime.datetime.now()
                access_token = token_response['access_token']
                expires_in = token_response['expires_in'] #seconds 
                expires = now + datetime.timedelta(seconds=expires_in)
                self.access_token = access_token
                self.access_token_exires = expires
                self.access_token_did_expire = expires < now
                return True #authorization sucessful 

        def get_token(self): #actually getting the token and making sure that it was not set to false(failed auth), the token has not expired, and that auth has not been preformed
                auth_done = self.do_auth()
                if not auth_done:
                        raise Exception("Auth failed")
                token = self.access_token
                expires = self.access_token_exires
                now = datetime.datetime.now()
                if expires < now:
                        self.do_auth()
                        return self.get_token()
                elif token == None:
                        self.do_auth()
                        return self.get_token()
                return token

        def get_resource_header(self): #formatting header for resource api call
                acess_token = self.get_token()
                header = {
                        'Authorization': f'Bearer {acess_token}'
                }
                return header

        def get_resource(self, lookup_id, resource_type='albums', version='v1', op='/'): #actually making the api call using the header and returning the json from the api call. Needs the ID of what is being searched, the type of data that is being requested and the api version. op is because the getting several track featues uses a question mark in it, it will default to '/' 
                endpoint = f'https://api.spotify.com/{version}/{resource_type}{op}{lookup_id}'
                header = self.get_resource_header()
                r = requests.get(endpoint, headers=header)
                if r.status_code not in range(200,299):
                        return {}
                return r.json()

        def get_album(self, _id): #calls the get_resource function with the argument of album as the resource type
                return self.get_resource(_id, resource_type='albums')
        
        def get_artist(self, _id): #calls the get_resource function with the argument of artist as the resource type
                return self.get_resource(_id, resource_type='artists')

        def get_features(self, _id): #calls the get_resource function with the argument of audio-feartures as the resource type
                return self.get_resource(_id, resource_type='audio-features', op='?ids=')


        def base_search(self, query, search_type='album'): #simple search that returns all resuls
                #example:: spotify.base_search('Time', search_type='track')
                acess_token = self.get_token()
                header = self.get_resource_header()
                endpoint = 'https://api.spotify.com/v1/search'
                lookup_url = f'{endpoint}?{query}'
                r = requests.get(lookup_url, headers=header)
                if r.status_code not in range(200,299):
                        return {}
                return r.json()


        def search(self, query=None, operator=None, operator_query = None, search_type='album'): #advanced search that allows for filerting and specific queries...uses base_search to preform the search
                # example1:: spotify.search({'track': 'Clocks', 'artist': 'Coldplay'}, search_type='track')...will search for Clocks by artist Coldplay
                # example2:: spotify.search(query='Danjer', operator='NOT', operator_query='Zone', search_type='track')...will search for danger but not danger zone
                if query == None:
                        raise Exception('Query not given')
                if isinstance(query,dict):
                        query= ' '.join([f'{k}:{v}' for k,v in query.items()])
                if operator != None and operator_query != None:
                        if operator.lower() == "or" or operator.lower() == "not":
                                operator = operator.upper()
                                if isinstance(operator_query, str):
                                        query = f'{query} {operator} {operator_query}'
                query_params = urlencode({'q': query, 'type': search_type.lower()})
                return self.base_search(query_params)

        def get_album_tracks(self, search): #returns a string of the track ids
                ids = ''
                if(search['tracks']['total'] == 0):
                        return ids
                albid = search['tracks']['items'][0]['album']['id']
                # print(albid)
                alb = spotify.get_album(albid)
                num_tracks = alb['total_tracks']
                for i in range(num_tracks):
                        ids+=(alb['tracks']['items'][i]['id'])+','

                return ids[:-1]

        def avg_features(self, features_in): #returns np array with avg of features for the entire album
                alb_fea = np.zeros(11, dtype=float)

                if(features_in['audio_features'][0] == None):
                        return np.array(alb_fea)
                
                num_tracks = len(features_in['audio_features'])
                
                for i in range(num_tracks): #sum of all the features
                        if(features_in['audio_features'][i] == None):
                                return alb_fea
                        alb_fea[0] += features_in['audio_features'][i]['danceability']
                        alb_fea[1] += features_in['audio_features'][i]['energy']
                        alb_fea[2] += features_in['audio_features'][i]['key']
                        alb_fea[3] += features_in['audio_features'][i]['loudness']
                        alb_fea[4] += features_in['audio_features'][i]['mode']
                        alb_fea[5] += features_in['audio_features'][i]['speechiness']
                        alb_fea[6] += features_in['audio_features'][i]['acousticness']
                        alb_fea[7] += features_in['audio_features'][i]['instrumentalness']
                        alb_fea[8] += features_in['audio_features'][i]['liveness']
                        alb_fea[9] += features_in['audio_features'][i]['valence']
                        alb_fea[10] += features_in['audio_features'][i]['tempo']
                
                alb_fea = [i/num_tracks for i in alb_fea] #take the avg by dividing each feature by the number of tracks

                return np.array(alb_fea)

        def create_mat(self):
                #get the list of titles of movies:
                data = read_csv("n_movies.csv")
                titles = data['Title'].tolist()

                ret = []

                f = open("temp.txt", "w")

                for i in range(4802,len(titles)):
                        search_res = spotify.search({'album': titles[i]}, search_type='track')
                        track_ids = spotify.get_album_tracks(search_res)
                        feat = spotify.get_features(track_ids)
                        alb_feat = spotify.avg_features(feat)
                        # ret.append(alb_feat)
                        np.savetxt(f, alb_feat)
                        print(i+1, titles[i])

                f.close()
                return np.asarray(ret)

        def cos_array(self, mat): #takes in one 2d np array
                dot = np.dot(mat, mat.T)
                diag = np.diag(dot)
                diag_inv = 1 / diag

                diag_inv[np.isinf(diag_inv)] = 0
                mag_inv = np.sqrt(diag_inv)
                cos_mat = dot * mag_inv
                cos_mat = cos_mat.T * mag_inv


                #need to take out the similarites to self
                for i in range(len(mat)):
                        for j in range(len(mat)):
                                if i == j:
                                        cos_mat[i][j] = 0

                return cos_mat


        def get_top_indx(self,sim_mat,n):
                rec_mat = np.zeros(shape=(4803,n*2+1),dtype=int)
                for i in range(4803):
                        top_indx = sorted(range(len(sim_mat[i,:])), key = lambda sub: sim_mat[i,:][sub])[-n:]
                        top_indx.reverse()
                        top_indx+=sorted(range(len(sim_mat[i,:])), key = lambda sub: sim_mat[i,:][sub])[:n+1]
                        rec_mat[i,:] = top_indx


                return rec_mat
        
        # def get_top_names(self, idx):



id = '981213db74a44914b7b9e753e2bc1eea' #spotify id
secret = 'b5139c4b81db4d1d9a7c706b999639a9' #spotify secret key
spotify = spotify_api(id, secret) #making an instance of the class

#create features mat
# c_mat = spotify.create_mat()


feat_array = np.loadtxt("array.txt").reshape(4803,11)
cos_mat = spotify.cos_array(feat_array)
np.save('spot_cos.npy', cos_mat)


rec_mat = spotify.get_top_indx(cos_mat,50)
np.save('spot_rec.npy', rec_mat)


#test search
# search_res = spotify.search({'album': "Shanghai Calling"}, search_type='track')
# aid = spotify.get_album_tracks(search_res)
# fe = spotify.get_features(aid)
# av = spotify.avg_features(fe)




# @app.route('/')
# def index():
#         return render_template('home.html', p = av)

# if __name__ == '__main__':
#     app.run(debug = True)