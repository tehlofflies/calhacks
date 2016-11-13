import requests

base_url = "http://api.musixmatch.com/ws/1.1/"

# MusixMatch API key, should be an environment variable
MUSIXMATCH_API_KEY = None
if('MUSIXMATCH_API_KEY' in os.environ):
    MUSIXMATCH_API_KEY = os.environ['MUSIXMATCH_API_KEY']

response  = requests.get(base_url, headers=headers)
response_json = response.json()

print response_json

