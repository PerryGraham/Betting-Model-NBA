import pandas as pd
import numpy as np
import statistics

gamesdata = pd.read_csv("data/cleandata.csv")
gamesdata2017 = pd.read_csv("data/games.csv")

# For having data for first 5 games of 2018 season 
gamesdata2017 = gamesdata2017.loc[gamesdata2017.SEASON >= 2017]

pt = gamesdata2017.PTS_home + gamesdata2017.PTS_away
gamesdata2017["point_total"] = pt
# Only need these columns for adding new feature
features_games = [
    "GAME_DATE_EST",
    "HOME_TEAM_ID",
    "VISITOR_TEAM_ID",
    "point_total",
]
gamesdata2017 = gamesdata2017[features_games].copy()

avgtotal_home = []
avgtotal_away = []
for ind in range(len(gamesdata)):
    date = gamesdata["GAME_DATE_EST"][ind]
    hteam = gamesdata["HOME_TEAM_ID"][ind]
    # When they are the home team 
    match_stats = gamesdata.loc[
        (gamesdata.GAME_DATE_EST < date) & (gamesdata.HOME_TEAM_ID == hteam)
    ]
    # When they are the visitor team
    match_stats_away = gamesdata.loc[
        (gamesdata.GAME_DATE_EST < date) & (gamesdata.VISITOR_TEAM_ID == hteam)
    ]
    # Home team 5 home games 
    if not match_stats.empty:
        prevgamescount = len(match_stats.index)  # How many games have been played
    if match_stats.empty or prevgamescount < 5:
        # If there are less than 5, then go back to the previous season and take the average
        lastseas = gamesdata2017.loc[
            (gamesdata2017.GAME_DATE_EST < date) & (gamesdata2017.HOME_TEAM_ID == hteam)
        ]
        lastseas10 = lastseas.iloc[:10]
        avglast5home = lastseas.point_total.mean(axis=0)
    else:
        only5 = match_stats.iloc[:10]
        avglast5home = only5.point_total.mean(axis=0)

    avgtotal_home.append(avglast5home)

    # Home team 5 away games
    if not match_stats_away.empty:
        prevgamescount = len(match_stats.index)  # How many games have been played
    if match_stats_away.empty or prevgamescount < 5:
        # If there are less than 5, then go back to the previous season and take the average
        lastseas = gamesdata2017.loc[
            (gamesdata2017.GAME_DATE_EST < date) & (gamesdata2017.VISITOR_TEAM_ID == hteam)
        ]
        lastseas10 = lastseas.iloc[:10]
        avglast5home = lastseas.point_total.mean(axis=0)
    else:
        only5 = match_stats.iloc[:10]
        avglast5home = only5.point_total.mean(axis=0)

    avgtotal_away.append(avglast5home)


avg_t = []
for i in range(len(avgtotal_home)):
    avg_t.append((avgtotal_home[i] + avgtotal_away[i]) / 2) 

gamesdata["avgpointtotal_home"] = avg_t

aavgtotal_home = []
aavgtotal_away = []
for ind in range(len(gamesdata)):
    date = gamesdata["GAME_DATE_EST"][ind]
    hteam = gamesdata["VISITOR_TEAM_ID"][ind]
    # When they are the home team 
    match_stats = gamesdata.loc[
        (gamesdata.GAME_DATE_EST < date) & (gamesdata.HOME_TEAM_ID == hteam)
    ]
    # When they are the visitor team
    match_stats_away = gamesdata.loc[
        (gamesdata.GAME_DATE_EST < date) & (gamesdata.VISITOR_TEAM_ID == hteam)
    ]
    # Home team 5 home games 
    if not match_stats.empty:
        prevgamescount = len(match_stats.index)  # How many games have been played
    if match_stats.empty or prevgamescount < 5:
        # If there are less than 5, then go back to the previous season and take the average
        lastseas = gamesdata2017.loc[
            (gamesdata2017.GAME_DATE_EST < date) & (gamesdata2017.HOME_TEAM_ID == hteam)
        ]
        lastseas10 = lastseas.iloc[:10]
        avglast5home = lastseas.point_total.mean(axis=0)
    else:
        only5 = match_stats.iloc[:10]
        avglast5home = only5.point_total.mean(axis=0)

    aavgtotal_home.append(avglast5home)

    # Home team 5 away games
    if not match_stats_away.empty:
        prevgamescount = len(match_stats.index)  # How many games have been played
    if match_stats_away.empty or prevgamescount < 5:
        # If there are less than 5, then go back to the previous season and take the average
        lastseas = gamesdata2017.loc[
            (gamesdata2017.GAME_DATE_EST < date) & (gamesdata2017.VISITOR_TEAM_ID == hteam)
        ]
        lastseas10 = lastseas.iloc[:10]
        avglast5home = lastseas.point_total.mean(axis=0)
    else:
        only5 = match_stats.iloc[:10]
        avglast5home = only5.point_total.mean(axis=0)

    aavgtotal_away.append(avglast5home)


aavg_t = []
for i in range(len(avgtotal_home)):
    aavg_t.append((aavgtotal_home[i] + aavgtotal_away[i]) / 2) 
    
gamesdata["avgpointtotal_away"] = aavg_t

mean = ((gamesdata.avgpointtotal_away + gamesdata.avgpointtotal_home) / 2)
gamesdata["meanpointtotal"] = mean 

#print(gamesdata)
gamesdata.to_csv(r"data/cleandata.csv", index=False)
print("done")


