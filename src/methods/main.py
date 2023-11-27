import ast
import requests
import json
import math

api_key = ""
name = "Maustach"

start_url_summoner = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
url_summoner = start_url_summoner + name + "?api_key=" + api_key

reponse_summoner = requests.get(url_summoner)
reponse_summoner_as_json = reponse_summoner.json()

summonerID = reponse_summoner_as_json['id']
accountId = reponse_summoner_as_json['accountId']
puuid = reponse_summoner_as_json['puuid']
summonerLevel = reponse_summoner_as_json['summonerLevel']

start_url_match = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/"
end_url_match = "/ids?start=0&count=20&api_key="
url_match = start_url_match + puuid + end_url_match + api_key

reponse_match = requests.get(url_match)
match_text: str = reponse_match.text
match_text: list = ast.literal_eval(match_text)


def get_winrate():
    win = 0
    for i in match_text:
        match_id = "https://europe.api.riotgames.com/lol/match/v5/matches/" + \
            i + "?api_key=" + api_key
        reponse_get_match_by_id = requests.get(match_id)
        match_by_id_text = reponse_get_match_by_id.text
        match_by_id_text = json.loads(match_by_id_text)
        match_win = match_by_id_text["info"]["teams"][1]["win"]
        if match_win == True:
            win += 1
    print((win/20)*100)


get_winrate()
