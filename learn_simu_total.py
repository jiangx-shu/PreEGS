#!/usr/bin/python
# encoding: utf-8
#
# usage: python <$0> current_index
#
import sys
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn import svm,datasets
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from read import readdata
from features import DifferentialExpression
from features import BetweennessCentrality
from features import DegreeCentrality
from features import ClosenessCentrality
from features import ClusteringCoefficient
from features import DifferentialDegreeCentrality
from sklearn.model_selection import cross_val_score
import csv

# 文件夹base地址
#5_double 五维差异
#4_singel 四维特定形态

#basename = '/Users/jiaminsun/Downloads/paper/jiaxinpaper/codeall/DNARF/data/simulated_data/5_double_datasettest.csv'
basename = '/Users/Lenovo/Desktop/sun/data-new/simulated_data/5_double_datasettest.csv'
#clf_NN=RandomForestClassifier(max_depth=10,n_estimators=100,min_samples_split=5)


#clf_NN = GaussianNB()
#clf_NN = KNeighborsClassifier(n_neighbors=3)
#clf=XGBClassifier()

#clf_NN = LogisticRegression()
clf_NN = SVC(C=5.0,probability=True)

X=[]
x=[]
y=[]
Y=[]
with open(basename,'r') as file:
    reader = csv.reader(file)
    for arr in reader:
        for i, val in enumerate(arr):
            if val.strip() != '':
                arr[i] = float(val.strip(' '))
            else:
                arr[i] = 0
        x = arr[0:5]
        X.append(x)
        y=arr[6]
        Y.append(y)

X_train = np.array(X)
y_train = np.array(Y)

print(np.mean(cross_val_score(clf_NN, X_train, y_train, cv=10, scoring='accuracy')))
print(np.mean(cross_val_score(clf_NN, X_train, y_train, cv=10, scoring='precision')))
print(np.mean(cross_val_score(clf_NN, X_train, y_train, cv=10, scoring='recall')))
print(np.mean(cross_val_score(clf_NN, X_train, y_train, cv=10, scoring='f1')))