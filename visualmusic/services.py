import requests
import urllib2
import json
from watson_developer_cloud import AlchemyLanguageV1

# MusixMatch API key, should be an environment variable
MUSIXMATCH_API_KEY = "1c1fc693d1e8a99b3fcd0cd662753cb1" 
ALCHEMY_API_KEY=  "305fd46a1c555652ed509e9cb36d6292c7043af3"
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


## 5 emotions: "disgust", "fear". "joy", "sadness", "anger"
def get_sentiment(inputText):
	alchemy_language = AlchemyLanguageV1(api_key=ALCHEMY_API_KEY)
	responseString = alchemy_language.emotion( text=inputText)
	return responseString["docEmotions"]


def main():
	songs = {"lost": "temper trap", "9": "drake", "i'll be alright": "passion pit"}
	outfile = open('sentiments.txt', 'w')
	
	for item in songs.keys():
		song = item
		artist = songs[item]

		track_id = find_track(song, artist)

		lyrics = get_lyrics(track_id)

		outfile.write((''.join(json.dumps(get_sentiment(lyrics)) + ", ")))

	print "all good!"

	

main()


