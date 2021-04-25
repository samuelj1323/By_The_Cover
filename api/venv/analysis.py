
import pandas as pd
import numpy as np
from PIL import Image
import requests # to get image from the web
import json
import pickle
from collections import OrderedDict

movie_rec = np.load("data/poster_similarity.npy")
sound_rec = np.load("data/soundtrack_similarity.npy")

from tmdbv3api import TMDb, Movie
tmdb = TMDb()
tmdb.api_key = '49845592e66ad5dd9458d0b648bf41d4'
api_key = '49845592e66ad5dd9458d0b648bf41d4'
url = ""
df = pd.read_csv("data/title.csv")
movie = Movie()
def top_10_posters(moviename):
	movie_name = moviename
	movie_number = df[df['title']==movie_name].index.values[0]
	top_10_posters= np.argsort(movie_rec[movie_number])[-10:]
	top_10_posters = np.flip(top_10_posters)
	top_10_posters_list = []
	count = 1
	for i in top_10_posters:
		print(i, df.loc[[i]]['title'].item())
		id_number = df.loc[[i]]['id'].item()
		title = df.loc[[i]]['title'].item()
		m = movie.details(id_number)
		url = "https://image.tmdb.org/t/p/original/" +m.poster_path
		dicti = {"title" : title,
				"url" : url}
		y = json.dumps(dicti)
		top_10_posters_list.append(y)
		# Image_numpy = Image.open(requests.get(url, stream=True).raw)
		# Image_numpy.save("data/images/Movie{}.jpg".format(str(count)))
		# count += 1
	return top_10_posters_list

def bottom_10_posters(moviename):
	movie_name = moviename
	movie_number = df[df['title']==movie_name].index.values[0]
	bottom_10_posters= np.argsort(movie_rec[movie_number])[:10]
	bottom_10_posters = np.flip(bottom_10_posters)

	bottom_10_posters_list = []
	count = 1
	for i in bottom_10_posters:
		print(i, df.loc[[i]]['title'].item())
		id_number = df.loc[[i]]['id'].item()
		title = df.loc[[i]]['title'].item()
		m = movie.details(id_number)
		url = "https://image.tmdb.org/t/p/original/" +m.poster_path
		dicti = {"title" : title,
				"url" : url}
		y = json.dumps(dicti)
		bottom_10_posters_list.append(y)
		# Image_numpy = Image.open(requests.get(url, stream=True).raw)
		# Image_numpy.save("data/images/Movie{}.jpg".format(str(count)))
		# count += 1
	return bottom_10_posters_list

def top_10_soundtracks(moviename):
	movie_name = moviename
	movie_number = df[df['title']==movie_name].index.values[0]
	top_10_soundtracks= np.argsort(sound_rec[movie_number])[-10:]
	top_10_soundtracks = np.flip(top_10_soundtracks)
	top_10_soundtrack_list = []
	count = 1
	for i in top_10_soundtracks:
		id_number = df.loc[[i]]['id'].item()
		title = df.loc[[i]]['title'].item()
		m = movie.details(id_number)
		print(i, df.loc[[i]]['title'].item())
		url = "https://image.tmdb.org/t/p/original" + m.poster_path
		dicti = {"title" : title,
				"url" : url}
		y = json.dumps(dicti)
		top_10_soundtrack_list.append(y)
		# Image_numpy = Image.open(requests.get(url, stream=True).raw)
		# Image_numpy.save("data/images/Movie{}.jpg".format(str(count)))
		# count += 1
	return top_10_soundtrack_list
def bottom_10_soundtracks(moviename):
	movie_name = moviename
	movie_number = df[df['title']==movie_name].index.values[0]
	sound_rec[sound_rec == 0] = 10
	series = pd.Series(sound_rec[movie_number])
	bottom_10_soundtracks= series.argsort()[1:11]
	bottom_10_soundtrack_list = []
	count = 1
	for i in bottom_10_soundtracks:
		print(i, df.loc[[i]]['title'].item())
		id_number = df.loc[[i]]['id'].item()
		title = df.loc[[i]]['title'].item()
		m = movie.details(id_number)
		url = "https://image.tmdb.org/t/p/original" + m.poster_path
		dicti = {"title" : title,
				"url" : url}
		y = json.dumps(dicti)
		bottom_10_soundtrack_list.append(y)
		Image_numpy = Image.open(requests.get(url, stream=True).raw)
		Image_numpy.save("data/images/Movie{}.jpg".format(str(count)))
		count += 1
	return bottom_10_soundtrack_list
def sound_then_poster(moviename):
	movie_name = moviename
	movie_number = df[df['title']==movie_name].index.values[0]
	sound_then_poster= np.argsort(sound_rec[movie_number])[-10:]
	sound_then_poster= np.flip(sound_then_poster)
	poster_values = []
	for i in sound_then_poster:
		poster_values.append(movie_rec[movie_number][i])
	zipped_lists = zip(poster_values, sound_then_poster)
	sorted_pairs = sorted(zipped_lists)
	sound_then_poster_list = []
	tuples = zip(*sorted_pairs)
	poster_values, sound_then_poster = [ list(tuple) for tuple in  tuples]
	poster_values.reverse()
	sound_then_poster.reverse()
	count = 1
	for i in sound_then_poster:
		id_number = df.loc[[i]]['id'].item()
		title = df.loc[[i]]['title'].item()
		m = movie.details(id_number)
		print(i, df.loc[[i]]['title'].item())
		url = "https://image.tmdb.org/t/p/original" + m.poster_path
		dicti = {"title" : title,
				"url" : url}
		y = json.dumps(dicti)
		sound_then_poster_list.append(y)
		# Image_numpy = Image.open(requests.get(url, stream=True).raw)
		# Image_numpy.save("data/images/Movie{}.jpg".format(str(count)))
		# count += 1
	return sound_then_poster_list

# sound_then_poster("Shrek")
# json("top10movies": ["","",""],
# 	"bottom_10_movies": ["",""])
def analyze(moviename):
	all_functions = {"top_10_posters": top_10_posters(moviename),
					 "bottom_10_posters": bottom_10_posters(moviename),
					 "top_10_soundtracks": top_10_soundtracks(moviename),
					 "bottom_10_soundtracks": bottom_10_soundtracks(moviename),
					 "sound_then_poster": sound_then_poster(moviename)}
	final = json.dumps(all_functions)
	return final

# analyze("Shrek")