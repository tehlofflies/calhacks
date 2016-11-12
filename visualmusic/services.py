import requests

base_url = "http://api.musixmatch.com/ws/1.1/"
headers = {
	'apikey': '1c1fc693d1e8a99b3fcd0cd662753cb1'
}
response  = requests.get(base_url, headers=headers)
response_json = response.json()

print response_json

