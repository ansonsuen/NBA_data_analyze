# Data Science NBA player's Height: Project Overview
 * Created a tool that to acknowlege does Height really matter.
 * Information Scraped from officail NBA website
 * Engineered features from the text of each job description to quantify the value companies put on python, excel,and aws .
 * Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
 * Built a client facing API using flask
# Code and Resources Used 
<br >**Python Version**: 3.7<br/>
<br >**Packages**: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle<br/>
<br >**For Web Framework Requirements**: pip install -r requirements.txt<br/>
<br >**Scraper Article**: 'https://www.nba.com/players'<br/>
<br >**Flask Productionization**: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2<br />
# Web Scraping
* Player
* Team'
* Numbers
* Position
* Height
* Weight
* Last_Attedent
* Country
-Lately NBA all star's has added in the columns for all better overview.
# Data Cleaning 
* selection_type split  to what reigion all star
* split c to f to have a new columns, All_Star
* HT change to int with replace
* split R in year_nba _draft to have Year Of NBA Draft Status
* drop all na columns and rows, which does not exsit.



