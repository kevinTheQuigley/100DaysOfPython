import spotipy
from spotipy.oauth2 import SpotifyOAuth
from arsewards import arsewards_dict
import os

scope = "user-library-read"
os.environ["SPOTIPY_CLIENT_ID"]=arsewards_dict["spotify_client_id"]
os.environ["SPOTIPY_CLIENT_SECRET"]=arsewards_dict["spotify_client_id_secret"]
os.environ["SPOTIPY_REDIRECT_URI"]=arsewards_dict["SPOTIPY_REDIRECT_URI"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])