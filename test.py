from espn_api.basketball import League

LEAGUE_ID = 2142217092
YEAR = 2021
ESPN_2 = "AECox3HQX41Ekc%2Bjyoa6Vj4bWoIqI3uhRpyMRAhNIDKCary6Q3Q0IFToSQahGqCar%2F%2BaJq0UlQs%2B%2BoHjndhneXswVf%2BF1zLbBbJ2AwKd%2F1hZUY1Kjv884%2FElh4e19tNeK9DqAAyr9GYWJ0Fw5Z%2FUYKWdI48gCD1rR4CjKiZgpTqgk1Tm9ifkfC0TyzDYa%2Bda4a4VvLdsS6hYMuvCJm9acLENgXYBTqvZqBeOm7UySYVCw8lqwyjacW8gnpcw6T9igzOTlDxsjW6uYhu1yvbSvTp7"
SWID = "0FA8E20F-267F-4A5E-9630-7D28BABEF81C"


league = League(league_id=2142217092, year = 2021, espn_s2=ESPN_2, swid=SWID)

matchups = league.scoreboard(9)

matchup = matchups[0]

team = matchup.home_team

for i in range(len(team.roster)):
    print(team.roster[i].injuryStatus)