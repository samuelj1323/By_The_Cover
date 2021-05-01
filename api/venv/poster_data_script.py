from tmdbv3api import TMDb, Movie
import pandas as pd
import numpy as np
from PIL import Image
import urllib.request
import requests # to get image from the web
tmdb = TMDb()
tmdb.api_key = '49845592e66ad5dd9458d0b648bf41d4'
from skimage.io import imread,imsave
from skimage.color import rgb2gray
import base64
import cv2
import urllib
import pickle
import threading
from skimage import measure
import matplotlib.pyplot as plt
df = pd.read_csv("title.csv")

def thread_function(irange,length,image_vector_list):
	movie = Movie()
	# count = 0

	for i in range(irange[0], irange[1]):
	    try:
	        # count +=1 
	        # if (count > length):
	        #     break
	        id_number = df.loc[[i]]['id'].item()
	        # print(id_number)
	        m = movie.details(id_number)
	        url = "https://image.tmdb.org/t/p/original/" +m.poster_path
	        image_numpy = np.array(Image.open(requests.get(url, stream=True).raw).convert('L').resize((100,100)))
	        image_vector_list[i] = image_numpy
	        print(i, df.loc[[i]]['title'].item())
	        # print(image_numpy)

	    except Exception:
	    	image_numpy = np.array(Image.open("white.png").convert('L').resize((100,100)))
	    	print("!!!!!!!!!!!!Value not found!!!!!!!!!!!!!!!!!!")
	    	print(i, df.loc[[i]]['title'].item())
	    	image_vector_list[i] = image_numpy
	    	print("!!!!!!!!!!!!Value not found!!!!!!!!!!!!!!!!!!")

	    	continue

iteration = 300
length = 4800
image_vector_list = [0] * length

thread_ranges = [*range(0, length, iteration)]
# print(thread_ranges)
threads = list()
for i in thread_ranges:
	x = threading.Thread(target=thread_function, args=([i, i+iteration], length,image_vector_list))
	threads.append(x)
	x.start()
for index, thread in enumerate(threads):
    thread.join()


length = len(image_vector_list)
final_mat = np.zeros((length, length))


def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err
def compare_images(imageA, imageB):
	s = measure.compare_ssim(imageA, imageB)
	return s
def thread_function(final_mat, irange, length):
	for i in range(irange[0], irange[1]):
		for j in range(0, length):
			print(i,j)
			array_1 =image_vector_list[i]
			array_2 = image_vector_list[j]
			x = compare_images(array_1, array_2)
			if x != 1:
				final_mat[i][j] = x
			else:
				final_mat[i][j] = 0


iteration = 200
thread_ranges = [*range(0, length, iteration)]
# print(thread_ranges)
threads = list()
for i in thread_ranges:
	x = threading.Thread(target=thread_function, args=(final_mat, [i, i+iteration], length))
	threads.append(x)
	x.start()


for index, thread in enumerate(threads):
    thread.join()

no_poster_list = pickle.load( open( "no_poster.p", "rb" ) )

for i in range(0,len(sim_mat)):
	for j in range(0,len(sim_mat[i])):
		if i in no_poster_list:
			sim_mat[i][j] = 0
		elif j in no_poster_list:
			# print(i,j)
			sim_mat[i][j] = 0
		else:
			continue

np.save("data/poster_similarity.npy", sim_mat)