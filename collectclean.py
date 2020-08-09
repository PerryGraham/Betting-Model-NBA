import pandas as pd 
import numpy as np


gamesdata = pd.read_csv("data/games.csv")
recorddata = pd.read_csv("data/ranking.csv")

# Adds the total points scored in a game to the end of the dataframe
point_total= gamesdata.PTS_home + gamesdata.PTS_away
gamesdata["point_total"] = point_total

# Removing entries before 2018 season 
gamesdata = gamesdata.loc[gamesdata.SEASON >= 2018]
gamesdata.sort_values(by=["GAME_DATE_EST"])
gamesdata = gamesdata.reset_index()

# Removing unwanted features 
features_games = ["GAME_DATE_EST","HOME_TEAM_ID","VISITOR_TEAM_ID","SEASON","PTS_home","PTS_away","point_total"]
gamesdata = gamesdata[features_games].copy()
#print(gamesdata) -looks good 

features_record = ["TEAM_ID","SEASON_ID","STANDINGSDATE","G","W","L","W_PCT","HOME_RECORD","ROAD_RECORD"]
recorddata = recorddata[features_record].copy()

#print(recorddata) - SEASON_ID values are wrong

# Fixing recorddata season column
recorddata["SEASON_ID"] = recorddata["SEASON_ID"].apply(lambda x: x-20000)

# Removing entries before 2018 season rom recorddata
recorddata = recorddata.loc[recorddata.SEASON_ID >= 2018]
recorddata.sort_values(by=["SEASON_ID"])
recorddata = recorddata.reset_index()

# Matching data from rankings with the gamesdata file 
g=[]
w=[]
l=[]
wpc=[]
homerec=[]
roadrec=[]
for ind in range(len(gamesdata)): #for every entry in games data, it matches the previously reported stats for the team, season, and date before current. 
    date = gamesdata["GAME_DATE_EST"][ind]
    seas = gamesdata["SEASON"][ind]
    hteam = gamesdata["HOME_TEAM_ID"][ind]
    temp1 = recorddata.loc[(recorddata.STANDINGSDATE < date) & (recorddata.SEASON_ID == seas) & (recorddata.TEAM_ID == hteam)]
    if temp1.empty:
        temp2 = 0
    else:
        temp2 = (temp1.iloc[0]["G"])
        temp3 = (temp1.iloc[0]["W"])
        temp4 = (temp1.iloc[0]["L"])
        temp5 = (temp1.iloc[0]["W_PCT"])
        temp6 = (temp1.iloc[0]["HOME_RECORD"])
        temp7 = (temp1.iloc[0]["ROAD_RECORD"])
    g.append(temp2) #appends all the wanted values to lists in order to put into the main dataset
    w.append(temp3)
    l.append(temp4)
    wpc.append(temp5)
    homerec.append(temp6)
    roadrec.append(temp7)
#data is already matched in order of row, so just add the list as a column 
gamesdata["cgp"] = g
gamesdata["wins"] = w
gamesdata["losses"] = l
gamesdata["winpercent"] = wpc
gamesdata["homerecord"] = homerec
gamesdata["awayrecord"] = roadrec

# Checked missing values, there are none
#print (gamesdata.isnull().sum()) 
#gamesdata.info()
#print(gamesdata.columns)

# Saved the new data file as 'cleandata.csv'
gamesdata.to_csv(r'C:\git\free-money\data\cleandata.csv',index = False)