import unittest
from datetime import datetime, timedelta, date
import wwwFootballDataOrg

apiToken = ''


class TestWwwFootballDataOrg(unittest.TestCase):
    # ok
    def test_v2_competitions(self):
        json_response = wwwFootballDataOrg.v2_competitions()

        print('response : ' + str(json_response))

        print('count : ' + str(json_response['count']))

        print('competition id : ' + str(json_response['competitions'][0]['id']))

    # ok
    def test_v2_competitions_id(self):
        json_response = wwwFootballDataOrg.v2_competitions_id("2018")

        print('response : ' + str(json_response))

        print('id : ' + str(json_response['id']))

        print('area name : ' + str(json_response['area']['name']))

    # ok
    def test_v2_competitions_id_teams(self):
        json_response = wwwFootballDataOrg.v2_competitions_id_teams('2015')

        print('response : ' + str(json_response))

        print('count : ' + str(json_response['count']))

        print('competition id : ' + str(json_response['competition']['id']))

    # ok
    def test_v2_competitions_id_standings(self):
        competitions = [
            {
                "competition": "uefa_champions_league",
                "id": "2001"
            },
            {
                "competition": "primeira_liga",
                "id": "2017"
            },
            {
                "competition": "premier_league",
                "id": "2021"
            },
            {
                "competition": "ligue_1",
                "id": "2015"
            },
            {
                "competition": "eredivisie",
                "id": "2003"
            },
            {
                "competition": "bundesliga",
                "id": "2002"
            },
            {
                "competition": "serie_a_brazil",
                "id": "2013"
            },
            {
                "competition": "la_liga",
                "id": "2014"
            },
            {
                "competition": "championship",
                "id": "2016"
            },
            {
                "competition": "serie_a_italy",
                "id": "2019"
            },
            {
                "competition": "world_cup",
                "id": "2000"
            },
            {
                "competition": "european_championship",
                "id": "2018"
            }
        ]

        for competition in competitions:
            try:
                json_response = wwwFootballDataOrg.v2_competitions_id_standings(competition.get('id'))

                # print('response : ' + str(json_response))

                # print('competition area id : ' + str(json_response['competition']['area']['id']))

                print('standings for ' + competition.get('competition') + ': ' + str(json_response['standings']))

                # print('season id : ' + str(json_response['season']['id']))
            except Exception as e:
                print("error for competition : " + competition.get('competition') + " - " + str(e))

    # ok
    def test_v2_competitions_id_matches(self):
        json_response = wwwFootballDataOrg.v2_competitions_id_matches('2015')

        print('response : ' + str(json_response))

        print('count : ' + str(json_response['count']))

        print('competition code : ' + str(json_response['competition']['code']))

    # ok
    def test_v2_competitions_id_scorers(self):
        json_response = wwwFootballDataOrg.v2_competitions_id_scorers('2015')

        print('response : ' + str(json_response))

        print('count : ' + str(json_response['count']))

        print('competition plan : ' + str(json_response['competition']['plan']))

    # ok
    def test_v2_matches(self):
        json_response = wwwFootballDataOrg.v2_matches()

        print('response : ' + str(json_response))

        print('count : ' + str(json_response['count']))

        print('filters dateFrom : ' + str(json_response['filters']['dateFrom']))

    # ok
    def test_v2_matches_id(self):
        json_response = wwwFootballDataOrg.v2_matches_id('273731')

        print('response : ' + str(json_response))

        print('head2head numberOfMatches : ' + str(json_response['head2head']['numberOfMatches']))

        print('match competition name : ' + str(json_response['match']['competition']['name']))

    # ok
    def test_v2_teams_id_matches(self):
        json_response = wwwFootballDataOrg.v2_teams_id_matches('511')

        print('response : ' + str(json_response))

        print('count : ' + str(json_response['count']))

        print('matches competition name : ' + str(json_response['matches']))

    # ok
    def test_v2_teams_id(self):
        json_response = wwwFootballDataOrg.v2_teams_id('511')

        print('response : ' + str(json_response))

        print('id : ' + str(json_response['id']))

        print('activeCompetitions name : ' + str(json_response['activeCompetitions'][0]['name']))

    # ok
    def test_v2_areas(self):
        json_response = wwwFootballDataOrg.v2_areas()

        print('response : ' + str(json_response))

        print('count : ' + str(json_response['count']))

        print('areas name : ' + str(json_response['areas'][0]['name']))

    # ok
    def test_v2_areas_id(self):
        json_response = wwwFootballDataOrg.v2_areas_id('2000')

        print('response : ' + str(json_response))

        print('id : ' + str(json_response['id']))

        print('countryCode : ' + str(json_response['countryCode']))

    # ok
    def test_v2_players_id(self):
        json_response = wwwFootballDataOrg.v2_players_id('43512')

        print('response : ' + str(json_response))

        print('id : ' + str(json_response['id']))

        print('firstName : ' + str(json_response['firstName']))

    # ok
    def test_v2_players_id_matches(self):
        json_response = wwwFootballDataOrg.v2_players_id_matches('43512')

        print('response : ' + str(json_response))

        print('count : ' + str(json_response['count']))

        print('player name : ' + str(json_response['player']['name']))

    # ok
    def test_v2_competition_id_matches_filters_scheduled(self):
        today = datetime.now().strftime('%Y-%m-%d')
        today_more_days = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
        json_response = wwwFootballDataOrg.v2_competition_id_matches_filters(
            '2018', today, today_more_days, 'SCHEDULED')

        print('response : ' + str(json_response))

        print('count : ' + str(json_response['count']))

    # ok
    def test_v2_competition_id_matches_filters_finished(self):
        today = datetime.now().strftime('%Y-%m-%d')

        print('today : ' + today)

        past = (date.today() - timedelta(days=365)).strftime('%Y-%m-%d')

        print('past : ' + past)

        json_response = wwwFootballDataOrg.v2_competition_id_matches_filters(
            '2015',
            past,
            today,
            'FINISHED'
        )

        print('response : ' + str(json_response))

        print('count : ' + str(json_response['count']))


if __name__ == '__main__':
    unittest.main()
