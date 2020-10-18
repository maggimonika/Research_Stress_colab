# -*- coding: utf-8 -*-
"""Stress_Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18ZCkwEqyDgBnrRR8U4OnciKh1E1UOnJ_
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

df=pd.read_excel('research_response.xlsx')

"""# Data Preperation"""

df.head(10)

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()

df.columns

df['span_duration'] = df['span_duration'].astype(str)
df['source'] = df['source'].astype(str)

for col in df.columns:
  print(col)
  df[col] = label_encoder.fit_transform(df[col])

df.head(10)

df.describe()

import seaborn as sns

sns.pairplot(df)

y = df['Stressed']
X = df.drop('Stressed',axis=1)

y.head(5)

X.head(5)

"""# Spliting Data"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

"""# KNN"""

error_rate = []
for i in range(1,40):
 knn = KNeighborsClassifier(n_neighbors=i)
 knn.fit(X_train,y_train)
 pred_i = knn.predict(X_test)
 error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=5)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

# creating classfier
classifier = KNeighborsClassifier(n_neighbors = 3)

classifier.fit(X_train, y_train)

# Testing the classifier
y_pred = classifier.predict(X_test)

result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)

sns.heatmap(confusion_matrix(y_test, y_pred),annot=True)

result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print (result1)

result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)

"""# MLP"""

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(max_iter=300)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

clf.score(X_test, y_test)

result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)

sns.heatmap(confusion_matrix(y_test, y_pred),annot=True)

result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print (result1)

result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)

"""# SVM"""

from sklearn import svm

clf = svm.SVC()

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

clf.score(X_test, y_test)

result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)

sns.heatmap(confusion_matrix(y_test, y_pred),annot=True)

result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print (result1)

result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)

"""# Decision Tree"""

from sklearn import tree

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

clf.score(X_test, y_test)

result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)

sns.heatmap(confusion_matrix(y_test, y_pred),annot=True)

result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print (result1)

result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)

"""# Random Forest"""

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=10)

clf = clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

clf.score(X_test, y_test)

result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)

sns.heatmap(confusion_matrix(y_test, y_pred),annot=True)

result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print (result1)

result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)



"""# Navie Bayes"""

from sklearn.naive_bayes import GaussianNB

clf = RandomForestClassifier(n_estimators=10)

clf = clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

clf.score(X_test, y_test)

result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)

sns.heatmap(confusion_matrix(y_test, y_pred),annot=True)

result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print (result1)

result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)

"""# Association mining"""

df=pd.read_excel('research_response.xlsx')

df['span_duration'] = df['span_duration'].astype(str)
df['source'] = df['source'].astype(str)

df.head()

df.columns

df['Gender'].unique()

df.query('Gender == "Female"')['Gender'].agg(['nunique','count','size'])

df.query('Gender == "Male"')['Gender'].agg(['nunique','count','size'])

df['Stressed'].unique()

df.query('Stressed == "Sometimes"')['Stressed'].agg(['nunique','count','size'])

df.query('Stressed == "Very Often"')['Stressed'].agg(['nunique','count','size'])

df.query('Stressed == "Never"')['Stressed'].agg(['nunique','count','size'])

df.head(3)

df.query('Gender == "Male" and Sector == "Private"')['Gender'].count()

df.query('Gender == "Female" and Sector == "Public"')['Gender'].count()



