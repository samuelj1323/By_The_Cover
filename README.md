# By_The_Cover
The audiovisual recommender for movies that recommends similar movies based on poster and soundtrack.

## The Pitch
When was the last time you couldn't name a movie you'd like to watch? Probably all the time, however when was the last time you wanted to watch a movie, couldn't name the movie, but knew the general theme you'd like to explore. "Something like Star wars, or Batman" ... Enter By The Cover. This project will exercise similarity scores off of movie posters from the TMDB movie data base and spotify musical albums of the specified films. These similarities produce filters through the database described below.

## Prepping to build

The data required for this application is taken of the Spotify and TMDB APIs and processed.
The data is stored at -
https://drive.google.com/drive/folders/1IdomZaMeSSgH1NQBgc4bpwT7ZMUZOKJ8?usp=sharing

Download this data to By_The_Cover/api/venv/data


## Building the Project - This will require 2 terminals

In the first terminal
- `npm install`
- `npm start`

In the second terminal
- `cd api/venv`
- `export FLASK_APP="api.py"`
- `flask run`

Application will run on localhost:3000

Some good movies to test with this system are-
  * Star Trek IV: The Voyage Home
  * TRON: Legacy
  * Star Wars: Episode I - The Phantom Menace
  * The Lord of the Rings: The Two Towers
  * Mission: Impossible

[![react](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
[![javascript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
