# -*- coding: utf-8 -*-
"""ca-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DoVskgUu5834HzFU4mdIGdGdcWCIjyF0
"""

from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

iris=datasets.load_iris()
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2,random_state=42)
# model=LinearRegression()
# model=RandomForestRegressor(n_estimators=100)
# model=LogisticRegression()
model=KNeighborsClassifier(n_neighbors=3)
# model=GaussianNB()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
# mse=mean_squared_error(y_test,y_pred)
# print(mse)
ax=accuracy_score(y_test,y_pred)
cf=confusion_matrix(y_test,y_pred)
cr=classification_report(y_test,y_pred)
cl=float(input("Enter cl:"))
cw=float(input("Enter cw:"))
pl=float(input("Enter pl:"))
pw=float(input("Enter pw:"))
prdcls=model.predict([[cl,cw,pl,pw]])
prdsp=iris.target_names[prdcls]
print(prdsp)
print(f"accuracy:{ax}")
print(f"cf:{cf}")
print(f"cr:{cr}")

from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

iris=datasets.load_iris()
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2,random_state=42)
# model=LinearRegression()
# model=RandomForestRegressor(n_estimators=100)
# model=LogisticRegression()
# model=KNeighborsClassifier(n_neighbors=3)
# model=GaussianNB()
model=DecisionTreeClassifier()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
# mse=mean_squared_error(y_test,y_pred)
# print(mse)
ax=accuracy_score(y_test,y_pred)
cf=confusion_matrix(y_test,y_pred)
cr=classification_report(y_test,y_pred)
cl=float(input("Enter cl:"))
cw=float(input("Enter cw:"))
pl=float(input("Enter pl:"))
pw=float(input("Enter pw:"))
prdcls=model.predict([[cl,cw,pl,pw]])
prdsp=iris.target_names[prdcls]
print(prdsp)
print(f"accuracy:{ax}")
print(f"cf:{cf}")
print(f"cr:{cr}")