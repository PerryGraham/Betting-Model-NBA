
# This is a work in progress

current best MAE is ~15.00 with Lasso Regression

Sports betting predictive modelling project

By: PerryGraham

The purpose of this project is to predict the Over-Under of an NBA game. 

# Data collection:
Model data downloaded from Kaggle from [Nathan Lauga](https://www.kaggle.com/nathanlauga/nba-games). 
Betting line history data scraped from [SDQL](https://sdql.com/) using [scrapy](https://scrapy.org/)
# Data cleaning:
* Added a point total column (target)
* Exculded data before 2018 season 
* Removed null values
* Sorted by date 
* Combined data from team ranking history
* One-hot encoded team IDs and label encoded Season 
* Pre-processing and scaled 
# Data insight:
* Opened cleaned data file with Tableau to explore the dataset 
    + Median total points = 221
    + Upper hinge = 235, lower hinge = 168
# Feature engineering:
* Added mean total points from previous 25 home and 25 away games for each team in the matchup as a column. 
    * Explored performing different variations of this feature; taking the difference, taking the mean, etc. 
* At first I only used past 2 years of data, because I thought teams rosters change a lot it wouldnt makes sense to take longer periods of data, of teams that dont exist anymore. However, adding the last 10 years of data helped a lot in getting better results.
* Then I tried using less features (only ones with high correlation with the target, this actually got worse results across all the model types)
* I tried manually scaling all of the data to see if that would help get better result in any of the models
# Model fitting:
* The XGBoost resgression model currently yields the most accurate results out of all the regression models that I have tried
# Cross valiation:
* The most ideal way of testing this data would be using a leave-one-out method, because this is how the model would operate in practice.
    * However, for simplicity reasons I chose to use a 90:10 (train:test) split with no shuffling. This should yield good enough testing scores. 
# Results:
* After scraping the betting lines history and calculationg their mean absolute error, they have a 13.4 over the past 10 years and 13.8 in the last 2 years. 
