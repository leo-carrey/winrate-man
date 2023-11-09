import requests
import json

api_key = "RGAPI-0dae43a9-ee4c-4ed0-8b83-3cbf1f8ad226"
name = "Maustach"

start_url_summoner = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
url_summoner = start_url_summoner + name + "?api_key=" + api_key

reponse_summoner = requests.get(url_summoner)
reponse_summoner.json()

summonerID = reponse_summoner.json()['id']
accountId = reponse_summoner.json()['accountId']
puuid = reponse_summoner.json()['puuid']
summonerLevel = reponse_summoner.json()['summonerLevel']

start_url_match = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/"
end_url_match = "/ids?start=0&count=20&api_key="
url_match = start_url_match + puuid + end_url_match + api_key

reponse_match = requests.get(url_match)
reponse_match.json()

# print(summonerID)
# print(accountId)
# print(puuid)
# print(summonerLevel)
print(reponse_match)
