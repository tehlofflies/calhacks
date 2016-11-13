import requests
import urllib2
import json

# MusixMatch API key, should be an environment variable
MUSIXMATCH_API_KEY = "1c1fc693d1e8a99b3fcd0cd662753cb1" 
# if('MUSIXMATCH_API_KEY' in os.environ):
#     MUSIXMATCH_API_KEY = os.environ['MUSIXMATCH_API_KEY']

API_HOST = 'api.musixmatch.com'
API_SELECTOR = '/ws/1.1/'

def find_track(song_title, song_artist):
	''' find track and return its id '''

	method = "track.search"
	q_track = song_title.replace(" ", "%20")
	q_artist = song_artist.replace(" ", "%20")
	f_has_lyrics = "1"

	search_params = "%s?q_track=%s&q_artist=%s&f_has_lyrics=%s" % (method, q_track, q_artist, f_has_lyrics)
	auth = "&apikey={}".format(MUSIXMATCH_API_KEY)
	url = "http://%s%s%s%s" % (API_HOST, API_SELECTOR, search_params, auth)

	req = urllib2.Request(url)
	req.add_header("Accept", "application/json")
	response = urllib2.urlopen(req).read()
	parse = json.loads(response)

	# print json.dumps(parse, indent=4, sort_keys=True)
	return parse["message"]["body"]["track_list"][0]["track"]["track_id"]


def get_lyrics(track_id):
	''' get track lyrics using track id '''

	magic_number = 15953433
	method = "track.lyrics.get"

	search_params = "%s?track_id=%s" % (method, track_id)
	auth = "&apikey={}".format(MUSIXMATCH_API_KEY)
	url="http://%s%s%s%s" % (API_HOST, API_SELECTOR, search_params, auth)

	req = urllib2.Request(url)
	req.add_header("Accept", "application/json")
	response = urllib2.urlopen(req).read()
	parsed = json.loads(response)
	return parsed["message"]["body"]["lyrics"]["lyrics_body"]


def main():
	song = "back to december"
	artist = "taylor swift"

	track_id = find_track(song, artist)

	return get_lyrics(track_id)


