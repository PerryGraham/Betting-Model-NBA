
# This is a work in progress

current best MAE is 14.75 with RandomForestRegression

Sports betting predictive modelling project

By: PerryGraham & alden-august-wang

The initial purpose of this project is to predict the Over-Under of an NBA game. 

# Data collection:
Data downloaded from Kaggle from Nathan Lauga. 
# Data cleaning:
* Added a point total column
* Exculded data before 2018 season 
* Removed null values
* Sorted by date 
* Combined data from team ranking history
* Encoded team IDs and Season 
# Data insight & visuals:
* Opened cleaned data file with Tableau to explore the dataset 
    + Median total points = 221
    + Upper hinge = 235, lower hinge = 168
# Feature engineering:
* At first I only used past 2 years of data, because I thought since teams change a lot it wouldnt makes sense to take longer periods of data, of teams that dont exist anymore. However, adding the last 10 years of data helped a lot in getting better results
* Then I tried using less features (only ones with high correlation with the target, this actually got worse results across all the model types
* I tried manually scaling all of the data to see if that would help get better result in any of the models
* The random forest resgression model currently yields the most accurate results out of all the regression models that I have tried
# Model fitting:

# Cross valiation:

# Results:
