import json
from tabulate import tabulate

def main():
    path_to_data = "data/premier-2015-16.json"
    datas = get_match_datas(path_to_data)
    season = datas['name']
    matches = get_matches(datas['rounds'])
    teams = eval_matches(matches)
    teams_list = teams_dict_to_list(teams)
    teams_list.sort(reverse=True, key=sort_on)
    rank = [x + 1 for x in range(20)]
    print(f"{season} Report")
    print(tabulate(teams_list, headers="keys", showindex=rank))

def get_match_datas(path):
    with open(path) as f:
        content = json.load(f)

    return content

def get_matches(rounds):
    matches = []
    for round in rounds:
        round_matches = round['matches']
        for match in round_matches:
            matches.append(match)

    return matches

def eval_matches(matches):
    teams = {}
    for match in matches:
        team1 = match['team1']
        team2 = match['team2']
        score = match['score']['ft']
        if team1 not in teams:
            create_team(teams, team1)
        if team2 not in teams:
            create_team(teams, team2)

        if score[0] > score[1]:
            teams[team1]['points'] += 3
        elif score[1] > score[0]:
            teams[team2]['points'] += 3
        else: # tie
            teams[team1]['points'] += 1
            teams[team2]['points'] += 1
        
        teams[team1]['goals'] += score[0]
        teams[team2]['goals'] += score[1]

        teams[team1]['diff'] += score[0] - score[1]
        teams[team2]['diff'] += score[1] - score[0]

    return teams

def create_team(teams, name):
    teams[name] = {'points': 0, 'diff': 0, 'goals': 0}


def teams_dict_to_list(teams_dict):
    teams_list = []

    for team in teams_dict:
        teams_list.append({
            'team': team, 
            'points': teams_dict[team]['points'],
            'diff': teams_dict[team]['diff'],
            'goals': teams_dict[team]['goals'],
        })

    return teams_list

def sort_on(team):
    return team['points'], team['diff'], team['goals']


main()