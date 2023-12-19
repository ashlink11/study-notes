import pandas as pd

temperatures = [63, 64, 66, 70, 63, 61, 61, 57, 57, 61, 64, 64, 61, 57]

temperatures_df = pd.DataFrame(temperatures, columns=['temperature'])

print(temperatures_df)

# Pandas dataframe has several methods that calculate descriptive statistics. 

# mean
mean = temperatures_df['temperature'].mean()
print("Mean=", round(mean,2))

# median
median = temperatures_df['temperature'].median()
print("Median=", round(median,2))

# variance
variance = temperatures_df['temperature'].var()
print("Variance=", round(variance,2))

# standard deviation
stdeviation = temperatures_df['temperature'].std()
print("Standard Deviation=", round(stdeviation,2))

# describe - a useful function that calculates several different descriptive statistics
statistics = temperatures_df['temperature'].describe()
print("")
print ("Describe method")
print (statistics)


import matplotlib.pyplot as plt

# line chart
plt.plot(temperatures_df['temperature']) # plot

# setting a title for the plot, x-axis and y-axis
plt.title('Line plot of temperature data', fontsize=20) 
plt.xlabel('day')
plt.ylabel('temperature')

# show the plot
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

# creates temperature data for Zion. You don't need to know how this data is created. 
# The temperature data created for Zion will be unique to you. 
mean = random.randint(temperatures_df['temperature'].min(),temperatures_df['temperature'].max())
std_deviation = random.randint(round(temperatures_df['temperature'].std(),0),round(2*temperatures_df['temperature'].std(),0))
zion_temperatures = np.random.normal(mean, std_deviation, 25)
zion_temperatures = pd.DataFrame(zion_temperatures, columns=['temperature'])

# side-by-side boxplots require the two dataframes to be concatenated and require a variable identifying the data
temperatures_df['id'] = 'my_data'
zion_temperatures['id'] = 'zion_data'
both_temp_df = pd.concat((temperatures_df, zion_temperatures))

# sets a title for the plot, x-axis, and y-axis
plt.title('Boxplot for comparison', fontsize=20) 

# prepares the boxplot
sns.boxplot(x="id",y="temperature",data=both_temp_df)

# shows the plot
plt.show()












import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

# use gamma distribution to randomly generate 500 observations. 
shape, scale = 1.95, 2.5
tpcp = 100*np.random.gamma(shape, scale, 500)

# pandas library can be used to convert the array into a dataframe of rounded figures with the column name TPCP.
tpcp_df = pd.DataFrame(tpcp, columns=['TPCP'])
tpcp_df = tpcp_df.round(0)

# print the dataframe to see the first 5 and last 5 observations (note that the index of dataframe starts at 0).
print("TPCP data frame\n")
print(tpcp_df)

# create a figure for the plot. 
fig, ax = plt.subplots()

# create a histogram plot with 50 bins of TPCP population data. 
plt.hist(tpcp_df['TPCP'], bins=50)

# set a title for the plot, x-axis, and y-axis.
plt.title('TPCP population distribution', fontsize=20)
ax.set_xlabel('TPCP')
ax.set_ylabel('Frequency')

# show the plot.
plt.show()

# You can use the "mean" method of a pandas dataframe.
pop_mean = tpcp_df['TPCP'].mean()
print("Population mean =", round(pop_mean,2))


# use sample method of the dataframe to select a random sample, with replacement, of size 50.
tpcp_sample_df = tpcp_df.sample(50, replace=True)

# print the sample mean.
sample_mean = tpcp_sample_df['TPCP'].mean()
print("Sample mean =", round(sample_mean,2))


# run a for loop to repeat the process Step 4 one thousand times to select one thousand samples.
# save the mean of each sample that was drawn in a Python list called means_list.
means_list = []
for i in range(1000):
    tpcp_sample_df = tpcp_df.sample(50, replace=True)
    sample_mean = tpcp_sample_df['TPCP'].mean()
    means_list.append(sample_mean)
    
# create a Python dataframe of means.
means_df = pd.DataFrame(means_list, columns=['means'])
print("Dataframe of 1000 sample means\n")
print(means_df)


# create a figure for the plot. 
fig, ax = plt.subplots()

# create a histogram plot with 50 bins of 1,000 means. 
plt.hist(means_df['means'], bins=50)

# set a title for the plot, x-axis and y-axis.
plt.title('Distribution of 1000 sample means', fontsize=20) # title
ax.set_xlabel('Means')
ax.set_ylabel('Frequency')

# show the plot.
plt.show()


# calculate mean of the 1,000 sample means (this is called the grand mean or mean of the means).
mean1000 = means_df['means'].mean()
print("Grand Mean (Mean of 1000 sample means) =",round(mean1000,2))

# calculate standard deviation of the 1,000 sample means.
std1000 = means_df['means'].std()
print("Std Deviation of 1000 sample means =",round(std1000,2))

# print the probability that a specific mean is 450 or less for a Normal distribution with mean and standard deviation of 1,000 sample means.
prob_450_less_or_equal = st.norm.cdf(450, mean1000, std1000)
print("Probability that a specific mean is 450 or less =", round(prob_450_less_or_equal,4))















import pandas as pd
import numpy as np
import math
import scipy.stats as st

# create 50 randomly chosen values from a Normal distribution. (arbitrarily using mean=2.48 and standard deviation=0.50). 
diameters = np.random.normal(2.4800,0.500,50)

# convert the array into a dataframe with the column name "diameters" using pandas library.
diameters_df = pd.DataFrame(diameters, columns=['diameters'])
diameters_df = diameters_df.round(2)

# print the dataframe (note that the index of dataframe starts at 0).
print("Diameters data frame\n")
print(diameters_df)




# Python methods that calculate confidence intervals require the sample mean and the standard error as inputs.

# calculate the sample mean
mean = diameters_df['diameters'].mean()

# input the population standard deviation, which was given in Step 1.
std_deviation = 0.5000

# calculate standard error = standard deviation / sqrt(n)   where n is the sample size.
stderr = std_deviation/math.sqrt(len(diameters_df['diameters']))

# construct a 90% confidence interval.
conf_int_90 = st.norm.interval(0.90, mean, stderr)
print("90% confidence interval (unrounded) =", conf_int_90)
print("90% confidence interval (rounded) = (", round(conf_int_90[0], 2), ",", round(conf_int_90[1], 2), ")")
print("")

# construct a 99% confidence interval.
conf_int_99 = st.norm.interval(0.99, mean, stderr)
print("99% confidence interval (unrounded) =", conf_int_99)
print("99% confidence interval (rounded) = (", round(conf_int_99[0], 2), ",", round(conf_int_99[1], 2), ")")



from statsmodels.stats.weightstats import ztest

# run z-test hypothesis test for population mean. The value under the null hypothesis is 2.30.
test_statistic, p_value = ztest(x1 = diameters_df['diameters'],  value = 2.30)

print("z-test hypothesis test for population mean")
print("test-statistic =", round(test_statistic,2))
print("two tailed p-value =",round(p_value,6))
















import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
from IPython.display import display, HTML

nba_orig_df = pd.read_csv('nbaallelo.csv')
nba_orig_df = nba_orig_df[(nba_orig_df['lg_id']=='NBA') & (nba_orig_df['is_playoffs']==0)]
columns_to_keep = ['game_id','year_id','fran_id','pts','opp_pts','elo_n','opp_elo_n', 'game_location', 'game_result']
nba_orig_df = nba_orig_df[columns_to_keep]

# The dataframe for the assigned team is called assigned_team_df. 
# The assigned team is the Chicago Bulls from 1996-1998.
assigned_years_league_df = nba_orig_df[(nba_orig_df['year_id'].between(1996, 1998))]
assigned_team_df = assigned_years_league_df[(assigned_years_league_df['fran_id']=='Bulls')]
assigned_team_df = assigned_team_df.reset_index(drop=True)

display(HTML(assigned_team_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the data set =", len(assigned_team_df))






# Range of years: 2013-2015 (Note: The line below selects ALL teams within the three-year period 2013-2015. This is not your team's dataframe.
your_years_leagues_df = nba_orig_df[(nba_orig_df['year_id'].between(2013, 2015))]

# The dataframe for your team is called your_team_df.
# ---- TODO: make your edits here ----
your_team_df = your_years_leagues_df[(your_years_leagues_df['fran_id']=='Jazz')]
your_team_df = your_team_df.reset_index(drop=True)

display(HTML(your_team_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the data set =", len(your_team_df))



import seaborn as sns

# Histogram
fig, ax = plt.subplots()
plt.hist(your_team_df['pts'], bins=20)
plt.title('Histogram of points scored by the Utah Jazz in 2013 to 2015', fontsize=18)
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')
plt.show()
print("")

# Scatterplot
plt.title('Scatterplot of points scored by the Utah Jazz in 2013 to 2015', fontsize=18)
sns.regplot(your_team_df['year_id'], your_team_df['pts'], ci=None)
plt.show()


import seaborn as sns

# Histogram
fig, ax = plt.subplots()
plt.hist(assigned_team_df['pts'], bins=20)
plt.title('Histogram of points scored by the Bulls in 1996 to 1998', fontsize=18)
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')
plt.show()

# Scatterplot
plt.title('Scatterplot of points scored by the Bulls in 1996 to 1998', fontsize=18)
sns.regplot(assigned_team_df['year_id'], assigned_team_df['pts'], ci=None)
plt.show()



import seaborn as sns

# Side-by-side boxplots
both_teams_df = pd.concat((assigned_team_df, your_team_df))
plt.title('Boxplot to compare points distribution', fontsize=18) 
sns.boxplot(x='fran_id',y='pts',data=both_teams_df)
plt.show()
print("")

# Histograms
fig, ax = plt.subplots()
plt.hist(assigned_team_df['pts'], 20, alpha=0.5, label='Bulls')
plt.hist(your_team_df['pts'], 20, alpha=0.5, label='Jazz')
plt.title('Histogram to compare points distribution', fontsize=18) 
plt.xlabel('Points')
plt.legend(loc='upper right')
plt.show()





print("Points Scored by Your Team in Home Games (2013 to 2015)")
print("-------------------------------------------------------")

your_team_home_df = your_team_df[your_team_df['game_location']=='H'].copy()

# ---- TODO: make your edits here ----
mean = your_team_home_df['pts'].mean()
median = your_team_home_df['pts'].median()
variance = your_team_home_df['pts'].var()
stdeviation = your_team_home_df['pts'].std()
num_home_games = len(your_team_home_df)

print('Num home games: ', num_home_games)
print('Mean =', round(mean,3))
print('Median =', round(median,4))
print('Variance =', round(variance,3))
print('Standard Deviation =', round(stdeviation,3))



print("Points Scored by Your Team in Away Games (2013 to 2015)")
print("-------------------------------------------------------")

your_team_away_df = your_team_df[your_team_df['game_location']=='A'].copy()

# ---- TODO: make your edits here ----
mean = your_team_away_df['pts'].mean()
median = your_team_away_df['pts'].median()
variance = your_team_away_df['pts'].var()
stdeviation = your_team_away_df['pts'].std()

print('Mean =', round(mean,2))
print('Median =', round(median,2))
print('Variance =', round(variance,2))
print('Standard Deviation =', round(stdeviation,2))



print("Confidence Interval for Average Relative Skill in the years 2013 to 2015")
print("------------------------------------------------------------------------------------------------------------")

# Mean relative skill of all teams from the years 2013-2015
all_teams_mean = your_years_leagues_df['elo_n'].mean()
print('all teams mean: ', mean)

# Standard deviation of the relative skill of all teams from the years 2013-2015
stdev = your_years_leagues_df['elo_n'].std()
print('all teams stdev: ', stdev)

n = len(your_years_leagues_df)
print('number of games: ', n)


#Confidence interval
# ---- TODO: make your edits here ----
stderr = stdev/(n ** 0.5)
conf_int_95 = st.norm.interval(0.95, all_teams_mean, stderr)

print("95% confidence interval (unrounded) for Average Relative Skill (ELO) in the years 2013 to 2015 =", conf_int_95)
print("95% confidence interval (rounded) for Average Relative Skill (ELO) in the years 2013 to 2015 = (",  round(conf_int_95[0], 2),",", round(conf_int_95[1], 2),")")


print("\n")
print("Python Method to calculate probability that a team has Average Relative Skill LESS than the Average Relative Skill (ELO) of your team in the years 2013 to 2015")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------")

jazz_skill = your_team_df['elo_n']
jazz_mean = jazz_skill.mean()
print('jazz skill mean: ', jazz_mean)

choice1 = st.norm.sf(jazz_mean, all_teams_mean, stdev)
choice2 = st.norm.cdf(jazz_mean, all_teams_mean, stdev)
print('choice1 (sf): ', choice1)
print('choice2 (cdf): ', choice2)

# Pick the correct answer.
print("Which of the two choices (choice 1 or choice 2) is correct?  Choice 1 or Choice 2? Choice 2 is correct.")





print("Confidence Interval for Average Relative Skill in the years 1996 to 1998")
print("------------------------------------------------------------------------------------------------------------")

# Mean relative skill of all teams from the years 1996-1998
all_teams_mean_1996 = assigned_years_league_df['elo_n'].mean()
print('all teams mean: ', all_teams_mean_1996)

# Standard deviation of the relative skill of all teams from the years 1996-1998
stdev_1996 = assigned_years_league_df['elo_n'].std()
print('all teams stdev: ', stdev_1996)

n_1996 = len(assigned_years_league_df)
print('number of games: ', n_1996)


#Confidence interval
# ---- TODO: make your edits here ----
stderr_1996 = stdev_1996/(n_1996 ** 0.5)
conf_int_95_1996 = st.norm.interval(0.95, all_teams_mean_1996, stderr_1996)

print("95% confidence interval (unrounded) for Average Relative Skill (ELO) in the years 1996 to 1998 =", conf_int_95_1996)
print("95% confidence interval (rounded) for Average Relative Skill (ELO) in the years 1996 to 1998 = (",  round(conf_int_95_1996[0], 2),",", round(conf_int_95_1996[1], 2),")")

bulls_skill = assigned_team_df['elo_n']
bulls_mean = bulls_skill.mean()
print('bulls skill mean: ', bulls_mean)

bulls_stat_1 = st.norm.cdf(bulls_mean, all_teams_mean_1996, stdev_1996)
print('prob a team has less skill than bulls', bulls_stat_1)


















import pandas as pd
import numpy as np

# create 50 randomly chosen values from a normal distribution. (arbitrarily using mean=2.48 and standard deviation=0.500) 
diameters_sample1 = np.random.normal(2.48,0.500,50)

# convert the array into a dataframe with the column name "diameters" using pandas library
diameters_sample1_df = pd.DataFrame(diameters_sample1, columns=['diameters'])
diameters_sample1_df = diameters_sample1_df.round(2)

# create 50 randomly chosen values from a normal distribution. (arbitrarily using mean=2.50 and standard deviation=0.750) 
diameters_sample2 = np.random.normal(2.50,0.750,50)

# convert the array into a dataframe with the column name "diameters" using pandas library
diameters_sample2_df = pd.DataFrame(diameters_sample2, columns=['diameters'])
diameters_sample2_df = diameters_sample2_df.round(2)

# print the dataframe to see the first 5 observations (note that the index of dataframe starts at 0)
print("Diameters data frame of the first sample (showing only the first five observations)")
print(diameters_sample1_df.head())
print()
print("Diameters data frame of the second sample (showing only the first five observations)")
print(diameters_sample2_df.head())


from statsmodels.stats.proportion import proportions_ztest

# number of observations in the first sample with diameter values less than 2.20. 
count1 = len(diameters_sample1_df[diameters_sample1_df['diameters']<2.20])
print('count1: ', count1)


# number of observations in the second sample with diameter values less than 2.20. 
count2 = len(diameters_sample2_df[diameters_sample2_df['diameters']<2.20])
print('count2: ', count2)


# counts Python list
counts = [count1, count2]


# number of observations in the first sample
n1 = len(diameters_sample1_df)
print('n1: ', n1)

# number of observations in the second sample
n2 = len(diameters_sample2_df)
print('n2: ', n2)

phat1 = count1/n1
phat2 = count2/n2

print('p-hat_1_: ', phat1)
print('p-hat_2_: ', phat2)

phat = (count1 + count2)/(n1 + n2)

print('p-hat:', phat)

# n Python list
n = [n1, n2]

# perform the hypothesis test. output is a Python tuple that contains test_statistic and the two-sided P_value.
test_statistic, p_value = proportions_ztest(counts, n)

print("test-statistic =", round(test_statistic,2))
print("two tailed p-value =", round(p_value,4))





















import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
from IPython.display import display, HTML

nba_orig_df = pd.read_csv('nbaallelo.csv')
nba_orig_df = nba_orig_df[(nba_orig_df['lg_id']=='NBA') & (nba_orig_df['is_playoffs']==0)]
columns_to_keep = ['game_id','year_id','fran_id','pts','opp_pts','elo_n','opp_elo_n', 'game_location', 'game_result']
nba_orig_df = nba_orig_df[columns_to_keep]

# The dataframe for the assigned team is called assigned_team_df. 
# The assigned team is the Bulls from 1996-1998.
assigned_years_league_df = nba_orig_df[(nba_orig_df['year_id'].between(1996, 1998))]
assigned_team_df = assigned_years_league_df[(assigned_years_league_df['fran_id']=='Bulls')]
assigned_team_df = assigned_team_df.reset_index(drop=True)

display(HTML(assigned_team_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the dataset =", len(assigned_team_df))




# Range of years: 2013-2015 (Note: The line below selects all teams within the three-year period 2013-2015. This is not your team's dataframe.
your_years_leagues_df = nba_orig_df[(nba_orig_df['year_id'].between(2013, 2015))]

# The dataframe for your team is called your_team_df.
# ---- TODO: make your edits here ----
your_team_df = your_years_leagues_df[(your_years_leagues_df['fran_id']=='Jazz')]
your_team_df = your_team_df.reset_index(drop=True)

display(HTML(your_team_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the dataset =", len(your_team_df))





import scipy.stats as st

# Mean relative skill level of your team
mean_elo_your_team = your_team_df['elo_n'].mean()
print("Mean Relative Skill of your team in the years 2013 to 2015 =", round(mean_elo_your_team,2))


# Hypothesis Test
test_statistic, p_value = st.ttest_1samp(your_team_df['elo_n'],  1340)

print("Hypothesis Test for the Population Mean")
print("Test Statistic =", round(test_statistic,2)) 
print("P-value =", p_value) 
print("P-value (rounded) =", round(p_value,4))




import scipy.stats as st

# Mean points jazz
mean_pts_jazz = your_team_df['pts'].mean()
print("Mean pts of Jazz in the years 2013 to 2015 =", round(mean_pts_jazz,2))


# Hypothesis Test
test_statistic, p_value = st.ttest_1samp(your_team_df['pts'],  106)

print("Hypothesis Test for the Population Mean")
print("Test Statistic =", round(test_statistic,2)) 
print("P-value (rounded) =", round(p_value, 4)) 
print("P-value =", p_value) 




from statsmodels.stats.proportion import proportions_ztest

your_team_gt_102_df = your_team_df[(your_team_df['pts'] > 102)]

# Number of games won when your team scores over 102 points
counts = (your_team_gt_102_df['game_result'] == 'W').sum()

# Total number of games when your team scores over 102 points
nobs = len(your_team_gt_102_df['game_result'])

p = counts*1.0/nobs
print("Proportion of games won by your team when scoring more than 102 points in the years 2013 to 2015 =", round(p,4))


# Hypothesis Test
# ---- TODO: make your edits here ----
test_statistic, p_value = proportions_ztest(counts, nobs, 0.90, prop_var=0.90)

print("Hypothesis Test for the Population Proportion")
print("Test Statistic =", round(test_statistic,2)) 
print("P-value =", p_value)
print("P-value (rounded) =", round(p_value,4))




import scipy.stats as st

mean_elo_n_project_team = assigned_team_df['elo_n'].mean()
print("Mean Relative Skill of the assigned team in the years 1996 to 1998 =", round(mean_elo_n_project_team,2))

mean_elo_n_your_team = your_team_df['elo_n'].mean()
print("Mean Relative Skill of your team in the years 2013 to 2015  =", round(mean_elo_n_your_team,2))


# Hypothesis Test
# ---- TODO: make your edits here ----
test_statistic, p_value = st.ttest_ind(assigned_team_df['elo_n'], your_team_df['elo_n'])

print("Hypothesis Test for the Difference Between Two Population Means")
print("Test Statistic =", round(test_statistic,2)) 
print("P-value (rounded) =", round(p_value,4))
print("P-value =", p_value)




















import pandas as pd
from IPython.display import display, HTML

# read data from mtcars.csv data set.
cars_df_orig = pd.read_csv("https://s3-us-west-2.amazonaws.com/data-analytics.zybooks.com/mtcars.csv")

# randomly pick 30 observations from the data set to make the data set unique to you.
cars_df = cars_df_orig.sample(n=30, replace=False)

# print only the first five observations in the dataset.
print("Cars data frame (showing only the first five observations)\n")
display(HTML(cars_df.head().to_html()))




import matplotlib.pyplot as plt

# create scatterplot of variables mpg against wt.
plt.plot(cars_df["wt"], cars_df["mpg"], 'o', color='red')

# set a title for the plot, x-axis, and y-axis.
plt.title('MPG against Weight')
plt.xlabel('Weight (1000s lbs)')
plt.ylabel('MPG')

# show the plot.
plt.show()




import matplotlib.pyplot as plt

# create scatterplot of variables mpg against hp.
plt.plot(cars_df["hp"], cars_df["mpg"], 'o', color='blue')

# set a title for the plot, x-axis, and y-axis.
plt.title('MPG against Horsepower')
plt.xlabel('Horsepower')
plt.ylabel('MPG')

# show the plot.
plt.show()




# create correlation matrix for mpg, wt, and hp. 
# The correlation coefficient between mpg and wt is contained in the cell for mpg row and wt column (or wt row and mpg column).
# The correlation coefficient between mpg and hp is contained in the cell for mpg row and hp column (or hp row and mpg column).
mpg_wt_corr = cars_df[['mpg','wt','hp']].corr()
print(mpg_wt_corr)




from statsmodels.formula.api import ols

# create the multiple regression model with mpg as the response variable; weight and horsepower as predictor variables.
model = ols('mpg ~ wt+hp', data=cars_df).fit()
print(model.summary())
























import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
from IPython.display import display, HTML

# dataframe for this project
nba_wins_df = pd.read_csv('nba_wins_data.csv')

display(HTML(nba_wins_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the dataset =", len(nba_wins_df))




import scipy.stats as st

# ---- TODO: make your edits here ----
plt.plot(nba_wins_df['avg_elo_n'], nba_wins_df['total_wins'], 'o')

plt.title('Total Number of Wins by Average Relative Skill', fontsize=20)
plt.xlabel('Average Relative Skill')
plt.ylabel('Total Number of Wins')
plt.show()


# ---- TODO: make your edits here ----
correlation_coefficient, p_value = st.pearsonr(nba_wins_df['avg_elo_n'], nba_wins_df['total_wins'])

print("Correlation between Average Relative Skill and the Total Number of Wins ")
print("Pearson Correlation Coefficient =",  round(correlation_coefficient,4))
print("P-value =", p_value)




import statsmodels.formula.api as smf

# Simple Linear Regression
# ---- TODO: make your edits here ---
model1 = smf.ols('total_wins ~ avg_elo_n', nba_wins_df).fit()
print(model1.summary())




import scipy.stats as st

# ---- TODO: make your edits here ----
plt.plot(nba_wins_df['avg_pts'], nba_wins_df['total_wins'], 'o')

plt.title('Total Number of Wins by Average Points Scored', fontsize=20)
plt.xlabel('Average Points Scored')
plt.ylabel('Total Number of Wins')
plt.show()


# ---- TODO: make your edits here ----
correlation_coefficient, p_value = st.pearsonr(nba_wins_df['avg_pts'], nba_wins_df['total_wins'])

print("Correlation between Average Points Scored and the Total Number of Wins ")
print("Pearson Correlation Coefficient =",  round(correlation_coefficient,4))
print("P-value =", p_value)




import statsmodels.formula.api as smf

# Multiple Regression
model2 = smf.ols('total_wins ~ avg_pts + avg_elo_n', nba_wins_df).fit()
print(model2.summary())
model4 = smf.ols('total_wins ~ avg_elo_n', nba_wins_df).fit()
print(model4.summary())
model3 = smf.ols('total_wins ~ avg_pts', nba_wins_df).fit()
print(model3.summary())





final_model = smf.ols('total_wins ~ avg_elo_n + avg_pts + avg_elo_differential + avg_pts_differential', nba_wins_df).fit()
print(final_model.summary())


# Response variable
Y = nba_wins_df['total_wins']

plt.figure(figsize = (20, 16))
plt.tight_layout()

plt.subplot(2, 2, 1)
plt.scatter(x = nba_wins_df['avg_elo_n'], y = final_model.resid, color = 'blue', edgecolor = 'k')
xmin = min(nba_wins_df['avg_elo_n'])
xmax = max(nba_wins_df['avg_elo_n'])
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('$X_1$', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('$X_1$ vs. residuals', fontsize = 24)

plt.subplot(2, 2, 2)
plt.scatter(x = nba_wins_df['avg_pts'], y = final_model.resid, color = 'blue', edgecolor = 'k')
xmin = min(nba_wins_df['avg_pts'])
xmax = max(nba_wins_df['avg_pts'])
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('$X_2$', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('$X_2$ vs. residuals', fontsize = 24)

plt.subplot(2, 2, 3)
plt.scatter(x = nba_wins_df['avg_elo_differential'], y = final_model.resid, color = 'blue', edgecolor = 'k')
xmin = min(nba_wins_df['avg_elo_differential'])
xmax = max(nba_wins_df['avg_elo_differential'])
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('$X_3$', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('$X_3$ vs. residuals', fontsize = 24)

plt.subplot(2, 2, 4)
plt.scatter(x = nba_wins_df['avg_pts_differential'], y = final_model.resid, color = 'blue', edgecolor = 'k')
xmin = min(nba_wins_df['avg_pts_differential'])
xmax = max(nba_wins_df['avg_pts_differential'])
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('$X_3$', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('$X_4$ vs. residuals', fontsize = 24)
plt.show()

plt.figure(figsize = (8 ,5))
plt.subplot(1, 1, 1)
plt.scatter(x = final_model.fittedvalues, y = final_model.resid, color = 'blue', edgecolor = 'k')
xmin = min(Y)
xmax = max(Y)
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('Fitted values', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('Fitted values vs. residuals final model', fontsize = 24)
plt.show()


import statsmodels.graphics.gofplots as smg

plt.figure(figsize = (8 ,5))
plt.subplot(1, 1, 1)
fig = smg.qqplot(final_model.resid, line = '45', fit = 'True')

plt.xlabel('Theoretical quantiles')
plt.ylabel('Sample quantiles')
plt.title('Q-Q plot of normalized residuals for final model')
plt.show()

plt.figure(figsize = (8 ,5))
plt.subplot(1, 1, 1)
plt.scatter(x = model3.fittedvalues, y = model3.resid, color = 'blue', edgecolor = 'k')
xmin = min(Y)
xmax = max(Y)
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('Fitted values', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('Fitted values vs. residuals $X_2$ SLR model', fontsize = 24)
plt.show()

plt.figure(figsize = (8 ,5))
plt.subplot(1, 1, 1)
fig = smg.qqplot(model3.resid, line = '45', fit = 'True')

plt.xlabel('Theoretical quantiles')
plt.ylabel('Sample quantiles')
plt.title('Q-Q plot of normalized residuals for $X_2$ SLR model')
plt.show()












import pandas as pd

# read data from etf_returns.csv.
etf_returns_df = pd.read_csv('etf_returns.csv')

# print etf returns data set.
print(etf_returns_df)





import scipy.stats as st

# save return data for individual sectors for input to f_oneway method.
etf_returns_financial = etf_returns_df['financial']
etf_returns_energy = etf_returns_df['energy']
etf_returns_technology = etf_returns_df['technology']

# print the outputs: the test statistic and the P-value.
test_statistic, p_value = st.f_oneway(etf_returns_financial, etf_returns_energy, etf_returns_technology)

print("test statistic =", test_statistic)
print("P-value =", p_value)





import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

# side-by-side boxplots require the three dataframes to be concatenated and a require variable identifying the type of ETF.
etf_returns_financial_df = etf_returns_df[['financial']]
etf_returns_financial_df = etf_returns_financial_df.rename(columns={"financial": "return"})
etf_returns_financial_df['ETF'] = 'financial'

etf_returns_energy_df = etf_returns_df[['energy']]
etf_returns_energy_df = etf_returns_energy_df.rename(columns={"energy": "return"})
etf_returns_energy_df['ETF'] = 'energy'

etf_returns_technology_df = etf_returns_df[['technology']]
etf_returns_technology_df = etf_returns_technology_df.rename(columns={"technology": "return"})
etf_returns_technology_df['ETF'] = 'technology'

# concatenate dataframes for the three ETFs.
all_etfs_df = pd.concat((etf_returns_financial_df, etf_returns_energy_df, etf_returns_technology_df))

# set a title for the plot, x-axis, and y-axis.
plt.title('Boxplot for comparison', fontsize=20) 

# prepare the boxplot.
sns.boxplot(x="ETF",y="return",data=all_etfs_df)

# show the plot.
plt.show()


























































