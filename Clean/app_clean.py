from flask import Flask, render_template
import numpy as np
import json

app = Flask(__name__)

#remember 0-49 top indx, 51-100 will be least similar in with the least similar being at index 51, where the the movie itself might be in the list of least similar becasuse the sim was set to 0.
def get_idx(titles,titles_in):
        names = titles_in.split(",")
        t_list = titles.tolist()
        titl_idx = []
        for i in range(len(names)):
                try:
                        idx = t_list.index(names[i])
                        titl_idx.append(idx)
                except ValueError:
                        continue
        return titl_idx
        
def k_near(rec, titles, idx):
        names = []
        for i in range(len(idx)):
                temp = []
                rec_idx = rec_mat[idx[i]]
                for j in range(0,50):
                        temp.append(titles[rec_idx[j]])
                names.append(temp)
        return json.dumps(names)

def k_furth(rec, titles, idx):
        names = []
        for i in range(len(idx)):
                temp = []
                rec_idx = rec_mat[idx[i]]
                for j in range(50,101):
                        if(idx[i] != rec_idx[j]):
                                temp.append(titles[rec_idx[j]])
                names.append(temp)
        return json.dumps(names)

rec_mat = np.load('spot_rec.npy')
titles = np.load('titles.npy', allow_pickle=True)
 

idx = get_idx(titles,"Avatar,Up")
test = k_furth(rec_mat,titles,idx)


@app.route('/')
def index():
        return render_template('home.html', p = test)

if __name__ == '__main__':
    app.run(debug = True)



