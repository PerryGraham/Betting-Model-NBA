from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.ensemble import RandomForestRegressor
import eli5
from eli5.sklearn import PermutationImportance
import pandas as pd

# Read the data
X_full = pd.read_csv("data/cleandata.csv")

# Obtain target and predictors 
y = X_full.point_total
X = X_full.drop(["GAME_DATE_EST","point_total"], axis=1)

# What percentage of the data is from this season vs last season 
Lastseason = len(X.loc[X.SEASON == 2018].index)
Thisseason = len(X.loc[X.SEASON == 2019].index)
ratio = round(Thisseason/Lastseason *100,2)
print ("{} % of the data is from 2018 season".format(ratio))
# 80-20 split would only leave 10% of the training data being used from the 2019 season
# Since teams change a lot during the season, we would like to have more data from this season when training
# However we do not was to reduce the power of our validation process
# We will be using a 85-15 train_test_split

# Break off validation set from training data 
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.85, test_size=0.15, random_state=0)

# Base model
first_model = RandomForestRegressor(n_estimators=50, random_state=1).fit(X_train,y_train)
perm = PermutationImportance(first_model, random_state=1).fit(X_valid, y_valid)
eli5.show_weights(perm, feature_names = X_valid.columns.tolist())
eli5.show_weights(perm, feature_names = X_valid.columns.tolist())
