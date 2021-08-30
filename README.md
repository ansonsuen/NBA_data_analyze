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
* Selection_type split  to what reigion all star
* Split c to f to have a new columns, All_Star
* HT change to int with replace
* Split R in year_nba _draft to have Year Of NBA Draft Status
* Drop all na columns and rows, which does not exsit.
# EDA
<br>I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.</br>
![alt text](https://user-images.githubusercontent.com/63040009/131342900-edf3b098-446f-427f-b9c4-b760cedead97.png)
![alt text](https://user-images.githubusercontent.com/63040009/131342906-38f59ff2-fb76-443d-b2c9-00fa8c3daa83.png)
![alt text](https://user-images.githubusercontent.com/63040009/131342903-9af89f36-8dfa-4621-8eb6-bc8c436445c5.png)
![alt text](https://user-images.githubusercontent.com/63040009/131342904-25335639-005a-484a-8bc0-ea873a969b11.png)
# Model Building
Intially, dummy variables are tranformed fromcategorical variable and splited the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

Three models:
Multiple Linear Regression – Baseline for the model
Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.





