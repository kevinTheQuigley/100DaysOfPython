import  requests 
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from arsewards import arsewards_dict


#scope = "user-library-read"
scope="playlist-modify-private",
os.environ["SPOTIPY_CLIENT_ID"]=arsewards_dict["spotify_client_id"]
os.environ["SPOTIPY_CLIENT_SECRET"]=arsewards_dict["spotify_client_id_secret"]
os.environ["SPOTIPY_REDIRECT_URI"]=arsewards_dict["SPOTIPY_REDIRECT_URI"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    show_dialog=True,
    cache_path = "token.txt",
    redirect_uri=arsewards_dict["SPOTIPY_REDIRECT_URI"],
    client_id=arsewards_dict["spotify_client_id"],
    client_secret=arsewards_dict["spotify_client_id_secret"]
    ))
user = sp.current_user()["id"]
date = "1995-10-01"
#date =input("What date would you like to make a billboard playlist for?\n Format: YYYY-MM-DD\n")

url = "https://www.billboard.com/charts/hot-100/"+date
#print(url)
res = requests.get(url).text
soup = BeautifulSoup(res, "html.parser")




songTitle= soup.select("li ul li h3")
songArtist= soup.select("li ul li span")
songTitles = []
songArtists = []


for i in range(100):
    songTitles.append(songTitle[i].getText().strip())
    songArtists.append(songArtist[i].getText().strip())

song = sp.search(q="artists:"+songArtists[0] +" track:"+songTitles[0], type="track",limit = 1)
playId = sp.user_playlist_create(user, "Billboard top 100 for "+date, public=True, collaborative=False, description='')

sp.playlist_add_item(playId)

print(songTitles)