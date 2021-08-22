import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv('NBA.csv')
df = df.drop(columns='Unnamed: 0')  # drop the unnamed column,that has no sense with only index

# play gonna seperate their name
# get out of the lbs in the weight
# changed height to int
df['Player'] = df['Player'].str.replace(r"([A-Z])", r" \1").str.strip()
df['Weight'] = df['Weight'].str.replace('lbs', '')
df['Height'] = df['Height'].replace(
    {'6-8': 203.2, '6-9': 205.74, '6-10': 208.28, '6-11': 210.82, '6-1': 185.42, "6-2": 187.96, '6-3': 90.50,
     '6-4': 193.04, '6-5': 195.5,'6-6': 198.12, '6-7': 200.66, '5-11': 180.34, '7-0': 213.36,'6-0':182.88})
df['Height']=df['Height'].astype('float64')
df['Weight']=df['Weight'].astype('float64')
df.to_csv('NBA_Data_cleaned')
