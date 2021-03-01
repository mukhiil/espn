from espn_api.basketball import League
import json


LEAGUE_ID = 2142217092
YEAR = 2021
ESPN_2 = "AECox3HQX41Ekc%2Bjyoa6Vj4bWoIqI3uhRpyMRAhNIDKCary6Q3Q0IFToSQahGqCar%2F%2BaJq0UlQs%2B%2BoHjndhneXswVf%2BF1zLbBbJ2AwKd%2F1hZUY1Kjv884%2FElh4e19tNeK9DqAAyr9GYWJ0Fw5Z%2FUYKWdI48gCD1rR4CjKiZgpTqgk1Tm9ifkfC0TyzDYa%2Bda4a4VvLdsS6hYMuvCJm9acLENgXYBTqvZqBeOm7UySYVCw8lqwyjacW8gnpcw6T9igzOTlDxsjW6uYhu1yvbSvTp7"
SWID = "0FA8E20F-267F-4A5E-9630-7D28BABEF81C"

with open('server/schedule.json') as file:
    schedule = json.load(file)



league = League(league_id=2142217092, year = 2021, espn_s2=ESPN_2, swid=SWID)
box = league.box_scores()
week  = league.get_team_data(1).wins + league.get_team_data(1).losses + league.get_team_data(1).ties + 3
total_games = week - 3
matchups = league.scoreboard(week)
print(matchups)
team_points = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0

}

team_names = {
    
    1: "Not Nibasingh",
    2: "Bigg Time Ballers",
    3: "Cooper",
    4: "Shrek's P3NIS",
    5: "FC apecelona",
    6: "Famsauce FC"

}


# function to get total points for each team
def total_team_points(league,team_points):
    for i in range(3,week):
        scoreboard = league.scoreboard(i)

        matchup_one = scoreboard[0]
        print()
        print()
        matchup_two = scoreboard[1]
        matchup_three = scoreboard[2]

        teams = [matchup_one.home_team, matchup_one.away_team, 
        matchup_two.home_team, matchup_two.away_team, 
        matchup_three.home_team, matchup_three.away_team]

        for j in range(len(teams)):

            current_team = teams[j]
            team_number = current_team.team_id

            points = 0

            if j == 0:
                points = max(matchup_one.home_final_score,matchup_one.home_team_live_score)
            
            elif j == 1:
                points = max(matchup_one.away_final_score, matchup_one.away_team_live_score)
                
            elif j == 2:
                points = max(matchup_two.home_final_score, matchup_two.home_team_live_score)

            elif j == 3:
                points = max(matchup_two.away_final_score, matchup_two.away_team_live_score)

            elif j == 4:
                points = max(matchup_three.home_final_score, matchup_three.home_team_live_score)

            elif j == 5:
                points = max(matchup_three.away_final_score, matchup_three.away_team_live_score)

            team_points[team_number] = team_points[team_number] + points

#function to get average points for each team
def average_team_points():
    
    ret_list = []

    for i in range(len(team_names)):
        avg_team_points = team_points[i + 1] / total_games
        avg_team_points = int(avg_team_points)
        ret_list.append(avg_team_points)

    return ret_list


total_team_points(league, team_points)
print(team_points)
print(average_team_points())

    
#get a team's projected points for a week
def projected_points_for_week(team_id,week):

    weekly_total = 0
    roster_length = len(league.get_team_data(team_id).roster)

    for i in range(roster_length):
        
        i_week = str(week)
        team = league.get_team_data(team_id).roster[i].proTeam
        times_played_weekly = schedule[i_week][team]
        times_played_weekly = int(times_played_weekly)

        if league.get_team_data(team_id).roster[i].injuryStatus == "DAY_TO_DAY":
            times_played_weekly = times_played_weekly - 1.5
        
        elif league.get_team_data(team_id).roster[i].injuryStatus == "OUT":
            times_played_weekly = 0

        full_player_list = league.get_team_data(team_id).roster[i].stats['002021']['avg']
        average_fantasy_points = full_player_list["FGM"]*2 + full_player_list["FGA"]*-1 + full_player_list["FTM"] + full_player_list["FTA"]*-1 + full_player_list["3PTM"] + full_player_list["REB"] + full_player_list["AST"]*2 + full_player_list["STL"]*4 + full_player_list["BLK"]*4 + full_player_list["TO"]*-2 + full_player_list["PTS"]
        weekly_points = times_played_weekly * average_fantasy_points

        
        
        weekly_total = weekly_total + weekly_points

    return weekly_total


def projected_points_for_all():

    projected_points = [projected_points_for_week(1,week),projected_points_for_week(2,week),projected_points_for_week(3,week),projected_points_for_week(4,week),projected_points_for_week(5,week),projected_points_for_week(6,week)]

    ret_dict = {
        team_names[1]: int(projected_points[0]),
        team_names[2]: int(projected_points[1]),
        team_names[3]: int(projected_points[2]),
        team_names[4]: int(projected_points[3]),
        team_names[5]: int(projected_points[4]),
        team_names[6]: int(projected_points[5])
    }

    return ret_dict

def projected_winners_for_week(week=week):
    ret_list = []
    matchups = league.scoreboard(week)
    for i in range(len(matchups)):
        home_team = matchups[i].home_team
        away_team = matchups[i].away_team

        home_team_points = projected_points_for_week(home_team.team_id,week)
        away_team_points = projected_points_for_week(away_team.team_id,week)

        if home_team_points > away_team_points:
            winner = home_team
        else:
            winner = away_team

        team_name = team_names[winner.team_id]
        
        ret_list.append(team_name)

    ret_dict = {
        "team1": ret_list[0],
        "team2": ret_list[1],
        "team3": ret_list[2]
    }
    
    return ret_dict

        

print(projected_winners_for_week())


