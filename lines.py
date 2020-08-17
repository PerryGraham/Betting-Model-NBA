import pandas as pd 

data = pd.read_csv("datascrape/bets.csv")

# The rows have duplicates because of home/away, so remove every other row
data = data[data.site == "home"]

# Adding points for both teams together
data["real_total"] = data.apply(
    lambda row: row.points + row['o:points'], axis=1
    )

# Calculating the difference between the line and outcome 
data["error"] = data.apply(
    lambda row: row.real_total - row.total, axis=1
)

# Making the error the absolute value
data["error"] = data.error.abs()

# Calculating mean absolute error between the lines and outcome 
l = len(data)
te = data.error.sum()
mae_lines = te / l

print ("MAE over last 10 years",mae_lines)

# For fun, lets see if the lines have gotten more accurate over time. 

per = int(len(data)/5)

# ~2010-2012 data
first20 = data[:per]

tef = first20.error.sum()
maef = tef / per
print("mae old",maef)

# ~2017-2019 data
last20 = data[-per:]

tel = last20.error.sum()
mael = tel / per
print("mae new",mael)
