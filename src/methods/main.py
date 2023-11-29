import ast
import requests
import json

api_key = "RGAPI-a0515db0-0fff-4942-a3d4-38fdff274c8d"
name = "maustach"

start_url_summoner = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
url_summoner = start_url_summoner + name + "?api_key=" + api_key

reponse_summoner = requests.get(url_summoner)
reponse_summoner_as_json = reponse_summoner.json()

summonerID = reponse_summoner_as_json['id']
accountId = reponse_summoner_as_json['accountId']
puuid = reponse_summoner_as_json['puuid']
summonerLevel = reponse_summoner_as_json['summonerLevel']

# start_url_match = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/"
# end_url_match = "/ids?start=0&count=20&api_key="
# url_match = start_url_match + puuid + end_url_match + api_key

# reponse_match = requests.get(url_match)
# match_text: str = reponse_match.text
# match_text: list = ast.literal_eval(match_text)


url_league_v4 = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerID + "?api_key=" + api_key
reponse_url_league_v4 = requests.get(url_league_v4)
reponse_url_league_v4_as_json = reponse_url_league_v4.json()

number_wins_flex = reponse_url_league_v4_as_json[0]["wins"]
number_losses_flex = reponse_url_league_v4_as_json[0]["losses"]

number_wins_solo = reponse_url_league_v4_as_json[1]["wins"]
number_losses_solo = reponse_url_league_v4_as_json[1]["losses"]

get_winrate_flex = (number_wins_flex / (number_wins_flex + number_losses_flex)) * 100
get_winrate_solo = (number_wins_solo / (number_wins_solo + number_losses_solo)) * 100

print(get_winrate_flex)
print(get_winrate_solo)