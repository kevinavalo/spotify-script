import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id=os.environ['SPOTIFY_ID']
client_pw=os.environ['SPOTIFY_PW']

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_pw)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


playlists = sp.user_playlists('kevinavalo')

for playlist in playlists:
	for i, playlist in enumerate(playlists['items']):
		print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
	if playlists['next']:
		playlists = sp.next(playlists)
	else:
		playlists = None