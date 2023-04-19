import spotipy
from spotipy.oauth2 import SpotifyClientCredentials # Manager de credenciales


client_id ="xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
client_secret ="xxxxxxxxxxxxxxxxxxxxxxxx"

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_uri = "spotify:playlist:5CTpBjOEEpEOJaYSICd1A7"

results = sp.playlist(playlist_uri)
tracks = results["tracks"]["items"]
song = {}

with open(r'lista.txt', mode='w') as f:

    for track in tracks:
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]

        song = (f'{track_name} : {artist_name} \n')
        f.write(song)
        #print(f"{track_name} - {artist_name}")
        print(song)
    f.close()



'''
with open(r'lista.txt', mode='w') as f:
     
     for i in song:
          f.write(i)
          print(i)

     f.close()              
          
'''


"""
for track in tracks:

    track_name = track["track"]["name"]
    print(track_name)


    mi_path = "../fichero.txt"
f = open(mi_path, 'a+')

for i in lista:
    f.write(i)
    f.close()
"""
