import requests
import json

api_key = "RGAPI-007e1f71-b690-44d8-9a5b-6a2e5d8676f0"
name = "Maustach"

start_url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
url1 = start_url + name + "?api_key=" + api_key

reponse = requests.get(url1)
reponse.json()

summonerID = reponse.json()['puuid']

print(summonerID)