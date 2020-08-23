# Sports betting predictive modelling project

By: PerryGraham

[Click here to view the notebook](https://github.com/PerryGraham/Betting-Model-NBA/blob/master/BettingModel.ipynb)

Everything is explained in details within the notebook, I suggest looking there. Here is a brief summary: 

The purpose of this project is to predict the Over-Under of an NBA game using past outcomes.  
There is a lot of variance in the total points scored in a game that predicting soley based on recent outcomes is not accurate. 

# Data collection:
* Model data downloaded from Kaggle from [Nathan Lauga](https://www.kaggle.com/nathanlauga/nba-games).   
* Betting line history data scraped from [SDQL](https://sdql.com/) using [scrapy](https://scrapy.org/)
# Data cleaning:
* Added a point total column (target)
* Exculded data before 2018 season 
* Removed null values
* Sorted by date 
* Combined data from team ranking history
* One-hot encoded team IDs and label encoded Season 
* Pre-processing and scaled 
# Data insight:
* Heat maps for correlations   
![](https://i.imgur.com/7LzJjOg.png)  
![](https://i.imgur.com/jQJIIUh.png)
# Feature engineering:
* Added mean total points from previous 25 home and 25 away games for each team in the matchup as a column. 
    * Explored performing different variations of this feature; taking the difference, taking the mean, etc. 
* At first I only used past 2 years of data, because I thought teams rosters change a lot it wouldnt makes sense to take longer periods of data, of teams that dont exist anymore. However, adding the last 10 years of data helped a lot in getting better results.
* Then I tried using less features (only ones with high correlation with the target, this actually got worse results across all the model types)
* I tried manually scaling all of the data to see if that would help get better result in any of the models
# Model fitting:
* The hyperoptimized XGBoost resgression model currently yields the most accurate results out of all the regression models that I have tried
# Cross valiation:
* The most ideal way of testing this data would be using a leave-one-out method, because this is how the model would operate in practice.
    * However, for simplicity reasons I chose to use a 90:10 (train:test) split with no shuffling. This should yield good enough testing scores. 
# Results:
* After scraping the betting lines history and calculationg their mean absolute error, they have a 13.4 over the past 10 years and 13.8 in the last 2 years. 
* The most accurate model has a 15.70 mae. This is 12% better than guess the mean of the previous season and 15% worse than the betting lines accuracy.  
![](https://i.imgur.com/x6kMLHt.png)
