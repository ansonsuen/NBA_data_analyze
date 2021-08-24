import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
df =pd.read_csv('eda_data.csv')

pd.set_option('display.max_columns',None)

df=df.drop(columns=['Unnamed: 0'])
df=df.dropna()
# relevant columns
df_model=df[['Year', 'Player', 'Pos', 'HT', 'WT', 'Team', 'Selection Type',
       'NBA Draft Status', 'Nationality', 'All_Star',
       'Year Of NBA Draft Status']]
#get dummy data
df_dum=pd.get_dummies(df_model)
#print(df_dum)
X=df_dum.drop('HT',axis=1)
y=df_dum.HT.values
#train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.13, random_state=42)
#multople linear regression
import statsmodels.api as sm
X_sm=X= sm.add_constant(X)
model=sm.OLS(y,X_sm)
#print(model.fit().summary())
from sklearn.linear_model import LinearRegression,Lasso
lm=LinearRegression()
lm.fit(X_train,y_train)
from sklearn.model_selection import cross_val_score
print(np.mean(cross_val_score(lm,X_train,y_train,scoring='neg_mean_absolute_error')))
#lasso regression
lm_l=Lasso(alpha=.13)
lm_l.fit(X_train,y_train)
print(np.mean(cross_val_score(lm_l,X_train,y_train,scoring='neg_mean_absolute_error')
))
alpha=[]
error=[]
for i in range(1,100):
    alpha.append(i/100)
    lml=Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lm_l,X_train,y_train,scoring='neg_mean_absolute_error')))
plt.plot(alpha,error)
#plt.show()
err=tuple(zip(alpha,error))
df_err=pd.DataFrame(err,columns=['alpha','error'])
print(df_err[df_err.error==max(df_err.error)])

#random forest
from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor()
print(np.mean(cross_val_score(rf,X_train,y_train,scoring='neg_mean_absolute_error')))

#Tune models GridserachCV
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,100,10), 'criterion':('mse','mae'),'max_features':('auto','sqrt','log2')}
gs=GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train,y_train)
print(gs.best_score_)
gs.best_params_
gs.estimator

#test ensembles
tpred_lm=lm.predict(X_test)
tpred_lml=lm_l.predict(X_test)
tpred_rf=gs.best_estimator_.predict(X_test)
from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(y_test,tpred_lm))
print(mean_absolute_error(y_test,tpred_lml))
print(mean_absolute_error(y_test,tpred_rf))
print(mean_absolute_error(y_test,(tpred_lm+tpred_rf)/2))