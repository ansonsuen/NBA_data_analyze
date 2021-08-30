from lxml.html.builder import A
from pandas import DataFrame
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
url='https://www.nba.com/players'
df =pd.read_html(url,header=0)
df=pd.DataFrame(np.concatenate(df),columns=['Player','Team','Numbers','Position','Height','Weight','Last_Attedent','Country'])
print(df.columns)
df=df.to_csv('NBA.csv')