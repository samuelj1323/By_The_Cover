
import pandas as pd
import numpy as np
from PIL import Image
import requests # to get image from the web
import json
import pickle

movie_rec = np.load("data/cleaned.npy")
spot_rec = np.load("data/spot_rec.npy")

from tmdbv3api import TMDb, Movie
tmdb = TMDb()
tmdb.api_key = '49845592e66ad5dd9458d0b648bf41d4'
url = ""
df = pd.read_csv("data/title.csv")
movie = Movie()
def top_10_movies(moviename):
	movie_name = moviename
	movie_number = df[df['title']==movie_name].index.values[0]
	top_10_movies= np.argsort(movie_rec[movie_number])[-10:]
	top_10_movies = np.flip(top_10_movies)

	top_10_movie_list = []
	count = 1
	for i in top_10_movies:
		# i = top_10_movies[x]
		# print(movie_rec[movie_number][i])
		id_number = df.loc[[i]]['id'].item()
		title = df.loc[[i]]['title'].item()
		# print(id_number, df.loc[[i]]['title'].item())
		m = movie.details(id_number)
		url = "https://image.tmdb.org/t/p/original/" +m.poster_path
		dicti = {"title" : title,
				"url" : url}
		y = json.dumps(dicti)
		top_10_movie_list.append(y)
		# Image_numpy = Image.open(requests.get(url, stream=True).raw)
		# Image_numpy.save("data/images/Movie{}.jpg".format(str(count)))
		# count += 1

	print(top_10_movie_list)
def bottom_10_movies(moviename):
	movie_name = moviename
	movie_number = df[df['title']==movie_name].index.values[0]
	bottom_10_movies= np.argsort(movie_rec[movie_number])[:10]
	bottom_10_movies = np.flip(bottom_10_movies)

	bottom_10_movies = []
	count = 1
	for i in bottom_10_movies:
		# i = top_10_movies[x]
		# print(movie_rec[movie_number][i])
		id_number = df.loc[[i]]['id'].item()
		title = df.loc[[i]]['title'].item()
		# print(id_number, df.loc[[i]]['title'].item())
		m = movie.details(id_number)
		url = "https://image.tmdb.org/t/p/original/" +m.poster_path
		dicti = {"title" : title,
				"url" : url}
		y = json.dumps(dicti)
		bottom_10_movies.append(y)
		# Image_numpy = Image.open(requests.get(url, stream=True).raw)
		# Image_numpy.save("data/images/Movie{}.jpg".format(str(count)))
		# count += 1

	# print(top_10_movie_list)



# 	print(top_10_movie_list)

# json("top10movies": ["","",""],
# 	"bottom_10_movies": ["",""])
top_10_movies("Avatar")
bottom_10_movies("Avatar")
