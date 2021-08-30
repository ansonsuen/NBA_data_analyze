import pandas as pd
import numpy as np
import re
pd.set_option('display.max_columns', None)

df=pd.read_csv('NBA All Star Games.csv')
#selection_type split  to what reigion all star
df['Selection Type']=df['Selection Type'].astype('str')

import re
#Type=df['Selection Type'].apply(lambda x:x.split('f')[0])
df['All_Star']= df['Selection Type'].apply(lambda x:x.replace('C', ' ').replace('F ', ' ').split()[0:2])
df['All_Star']= df['All_Star'].str.join(',')
df['All_Star']= df['All_Star'].str.replace(',',' ')
df['Selection Type']=df['Selection Type'].apply(lambda x:x.replace('Western All-Star',' ').replace('Eastern All-Star'," "))
#ht change to int with replace
df['HT']= df['HT'].replace( {'6-8': 203.2, '6-9': 205.74, '6-10': 208.28, '6-11': 210.82, '6-1': 185.42, "6-2": 187.96, '6-3': 190.50,
     '6-4': 193.04, '6-5': 195.5,'6-6': 198.12, '6-7': 200.66, '5-11': 180.34, '7-0': 213.36,'6-0':182.88,'7-1':215.90,'7-2':218.44,'7-3':220.98,'7-6':228.6,'5-9':175.26})

#split R year_nba _draft
df['NBA Draft Status']=df['NBA Draft Status'].astype('str')
df['Year Of NBA Draft Status']=df['NBA Draft Status'].apply(lambda x:x.replace('R',' ').split()[0])
df['NBA Draft Status']=df['NBA Draft Status'].apply(lambda x:x.split(' ')[1:])
df['NBA Draft Status']=df['NBA Draft Status'].str.join(',')
df['NBA Draft Status']=df['NBA Draft Status'].str.replace(',',' ')
df=df.drop(columns=['Unnamed: 9', 'Unnamed: 10',
       'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14',
       'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18',
       'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22',
       'Unnamed: 23', 'Unnamed: 24'])
print(df.isnull().sum())
df=df.dropna(axis='index',how='any')
print(df.isnull().sum())

df.to_csv('NBA_All_Star_Game_Data_cleaned')


