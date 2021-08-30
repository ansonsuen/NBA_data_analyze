import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv('NBA_All_Star_Game_Data_cleaned')
df['Team'] = df['Team'].astype('str')
df.boxplot(column=['Year Of NBA Draft Status'])
cor = df[['HT', 'WT']].corr()
df.HT.hist()
df.WT.hist()
sns.heatmap(df[['HT','WT','Year']].corr(),cmap='YlGnBu')
df.boxplot(column=['HT'])
plt.show()


df_cat = df[
    ['Pos', 'WT', 'HT', 'Selection Type', 'NBA Draft Status', 'Nationality', 'All_Star', 'Year Of NBA Draft Status']]
for i in df_cat[['Pos', 'HT', 'WT']].columns:
    cat_num = df_cat[i].value_counts()
    print("Graph for %s: total =%d" % (i, len(cat_num)))
    chart = sns.barplot(x=df_cat[i].value_counts().index, y=cat_num)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    plt.show()


print(pd.pivot_table(df,index='Pos',values='HT'))

print(pd.pivot_table(df,index=['Pos','Nationality'],values='HT',aggfunc='count'))
import dataframe_image as dfi
df1=pd.pivot_table(df,index=['Pos','Nationality','Year Of NBA Draft Status'],values='HT',aggfunc='count').sort_values('HT',ascending=False)
dfi.export(df1.head(10),'dataframe.png')
print(df.columns)
df_cat2 = df[['Pos', 'WT', 'Selection Type',
             'NBA Draft Status', 'Nationality', 'All_Star',
              'Year Of NBA Draft Status'
              ]]
for i in df_cat2.columns:
    print('')
    print(pd.pivot_table(df_cat, index=i, values='HT', aggfunc='count').sort_values('HT', ascending=False))
df.to_csv('eda_data.csv')