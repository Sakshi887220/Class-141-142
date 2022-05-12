from flask import Flask, jsonify, request

from storage import all_movies, liked_movies, not_liked_movies, did_not_watch
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
   

@app.route("/liked-movie", )
def liked_movie():
   
@app.route("/unliked-movie",)
def unliked_movie():
  

@app.route("/did-not-watch", )
def did_not_watch_view():
    

@app.route("/popular-movies")
def popular_movies():
   
@app.route("/recommended-movies")
def recommended_movies():
    
if __name__ == "__main__":
  app.run()
