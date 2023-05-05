import requests
from bs4 import BeautifulSoup
import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

date = input("Which year do you want to go back (Enter the date in the format of YYYY-MM-DD): ")
URL = "https://www.billboard.com/charts/hot-100"

# Checking to see if it's an actual date
if (len(date) != 10) or ("-" not in date):
    quit("Invalid Input")

response = requests.get(f"{URL}/{date}")
content = response.text
soup = BeautifulSoup(content, 'html.parser')
songs = soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
first_song = soup.find(name="a", class_="c-title__link lrv-a-unstyle-link").getText()  # Because i can't get the first song along with the others in the line above
first_song = first_song.replace("\t", "")
first_song = first_song.replace("\n", "")

songs.insert(0, first_song)

for song in songs[1:]:
    i = song.getText()
    index = songs.index(song)
    songs.pop(index)
    i = i.replace("\t", "")
    i = i.replace("\n", "")
    songs.insert(index, i)

print(songs)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=config.CLIENT_ID,
        client_secret=config.CLIENT_SECRET,
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    ))

user_id = sp.current_user()["id"]
year = date.split("-")[0]
songs_uris = []

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        songs_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        pass

print(songs_uris)


