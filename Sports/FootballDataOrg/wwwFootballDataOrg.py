import requests
import json

apiToken = ''


# requete l'endpoint /v2/competitions/
def v2_competitions():
    url = "http://api.football-data.org/v2/competitions"
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/competitions/{idCompetition}
def v2_competitions_id(idCompetition):
    url = "http://api.football-data.org/v2/competitions/" + idCompetition
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/competitions/{idCompetition}/teams
def v2_competitions_id_teams(idCompetition):
    url = "http://api.football-data.org/v2/competitions/" + idCompetition + "/teams"
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/competitions/{id}/standings
def v2_competitions_id_standings(idCompetition):
    url = "http://api.football-data.org/v2/competitions/" + idCompetition + "/standings"
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/competitions/{idCompetition}/matches
def v2_competitions_id_matches(idCompetition):
    url = "http://api.football-data.org/v2/competitions/" + idCompetition + "/matches"
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/competitions/{id}/scorers
def v2_competitions_id_scorers(idCompetition):
    url = "http://api.football-data.org/v2/competitions/" + idCompetition + "/scorers"
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/matches
def v2_matches():
    url = "http://api.football-data.org/v2/matches"
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/matches/{idMatch}
def v2_matches_id(idMatch):
    url = "http://api.football-data.org/v2/matches/" + idMatch
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/teams/{idTeam}/matches/
def v2_teams_id_matches(idTeam):
    url = "http://api.football-data.org/v2/teams/" + idTeam + "/matches/"
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/teams/{idTeam}
def v2_teams_id(idTeam):
    url = "http://api.football-data.org/v2/teams/" + idTeam
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/areas/
def v2_areas():
    url = "http://api.football-data.org/v2/areas/"
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/areas/{idArea}
def v2_areas_id(idArea):
    url = "http://api.football-data.org/v2/areas/" + idArea
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/players/{idPlayer}
def v2_players_id(idPlayer):
    url = "http://api.football-data.org/v2/players/" + idPlayer
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# Requete l'endpoint /v2/players/{idPlayer}/matches
def v2_players_id_matches(idPlayer):
    url = "http://api.football-data.org/v2/players/" + idPlayer + "/matches"
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response


# requete l'endpoint /v2/competitions/{id}/matches avec les filtres suivants : dateFrom={DATE} , dateTo={DATE},
# status={STATUS}
def v2_competition_id_matches_filters(idCompetition, dateFrom, dateTo, status):
    url = "http://api.football-data.org/v2/competitions/" + idCompetition \
          + "/matches?dateFrom=" + dateFrom \
          + "&dateTo=" + dateTo \
          + "&status=" + status
    payload = {}
    headers = {
        'X-Response-Control': 'full',
        'X-Auth-Token': apiToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text.encode('utf8'))
    return json_response
