from fastapi import FastAPI                  # Backend Framework
from fastapi.responses import CORSMiddleware # CORS header to allow specify headers only
from fastapi.responses import FileResponse   # Send a specifc HTML, CSS, & JS file to broswer
from fastapi.staticfiles import StaticFiles  # Serves a folder's files automatically
from pydantic import BaseModel               # Helps with type check and type conversion

import youtube_api as yt_api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class YoutubeToSpotify(BaseModel):
    name: str
    youtube_playlist_link: str

class SpotifyToYoutube(BaseModel):
    name: str
    username: str
    password: str
    spotify_playlist_link: str

""" Youtube API Endpoints """
@app.get("/youtube_playlist/{playlist_id}")
def playlist_endpoint(playlist_id: str):
    return yt_api.get_playlist_videos_title(playlist_id)

""" Spotify API Endpoints """
# @app.get("/spotify")
# def home():
#     return {"Spotify API"}

# Serve Webpages
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_home():
    return FileResponse("frontend/html/index.html")