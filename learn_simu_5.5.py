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
from features import BetweennessCentrality_2
from features import DegreeCentrality_2
from features import ClosenessCentrality_2
from features import ClusteringCoefficient_2
from features import DifferentialDegreeCentrality_2


# 文件夹base地址
basename = '/Users/jiaminsun/Downloads/paper/jiaxinpaper/codeall/DNARF/data/simulated_data/m3_0.05/rho3_0.1_'
# 网络1文件名
networkname1 = 'matrix1.txt'
# 网络2文件名
networkname2 = 'matrix2.txt'
# 网络1表达值文件名
expressionname1 = 'expression1.txt'
# 网络2表达值文件名
expressionname2 = 'expression2.txt'
# 关键基因列表
importantname = 'important.txt'
total_vec = []
total_y = []
dataset_total=[]
totalnum = 0
for num in range(1, 101):
    expression1 = []
    expression2 = []
    dexpression = []
    vec = []
    y = []

    for i in range(0, 100):
        expression1.append([])
        expression2.append([])
        dexpression.append(0)
        vec.append([])
        y.append(0)
    with open(basename + str(num) + '/' + expressionname1) as file:
        for line in file:
            data = line[:-1].split(',')
            for i in range(0, 100):
                expression1[i].append(float(data[i]))

    with open(basename + str(num) + '/' + expressionname2) as file:
        for line in file:
            data = line[:-1].split(',')
            for i in range(0, 100):
                expression2[i].append(float(data[i]))

    # for i in range(0, 100):
    #     dexpression[i] = DifferentialExpression_2.cal_de(expression1[i], expression2[i])

    G1, G2 = readdata.readdata(basename + str(num) + '/' + networkname1, basename + str(num) + '/' + networkname2)

    # BetweennessCentrality
    data = BetweennessCentrality_2.cal_bc(G1, G2)
    for x in data:
        vec[int(x) - 1].append(data[x])

    # ClosenessCentrality
    data = ClosenessCentrality_2.cal_cc(G1, G2)
    for x in data:
        vec[int(x) - 1].append(data[x])

    # ClusteringCoefficient
    data = ClusteringCoefficient_2.cal_cco(G1, G2)
    for x in data:
        vec[int(x) - 1].append(data[x])

    # DegreeCentrality
    data = DegreeCentrality_2.cal_dc(G1, G2)
    for x in data:
        vec[int(x) - 1].append(data[x])

    # DifferentialDegreeCentrality
    data = DifferentialDegreeCentrality_2.cal_ddc(G1, G2)
    for x in data:
        vec[int(x) - 1].append(data[x])

    # # DifferentialExpression
    # for i in range(0, 100):
    #     vec[i].append(dexpression[i])

    for x in vec:
        total_vec.append(x)

    # important
    with open(basename + str(num) + '/' + importantname) as file:
        for line in file:
            y[int(line)-1] = 1
            vec[int(line)-1].append(1)
            dataset_total.append(vec[int(line)-1])
    count_time=0
    #not important
    for count in range(1,101):
        if y[int(count-1)]==0 and (count_time<100):
            vec[int(count)-1].append(0)
            dataset_total.append(vec[int(count)-1])
            count_time=count_time+1
        elif count_time>100:
            break
        else:
         continue
    with open('/Users/jiaminsun/Downloads/paper/jiaxinpaper/codeall/DNARF/data/simulated_data/4_1_single_datasettest.csv','w+') as f:
        for vect in dataset_total:
            str_buffer = ''
            for elem in vect:
                str_buffer = str_buffer + str(elem) + ','
            f.writelines(str_buffer+'\n')
    for x in y:
        total_y.append(x)
    # print(dataset_total)
X = np.array(total_vec)
Y = np.array(total_y)
