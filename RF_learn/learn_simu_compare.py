from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn import preprocessing
from read import readdata
from features import DifferentialExpression
from features import BetweennessCentrality
from features import DegreeCentrality
from features import ClosenessCentrality
from features import ClusteringCoefficient
from features import DifferentialDegreeCentrality

# 文件夹base地址
basename = '/Users/jiaminsun/Downloads/paper/jiaxinpaper/codeall/DNARF/data/simulated_data/0.1-0.5/rho_0.1_'
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

for num in range(1, 2):
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

    for i in range(0, 100):
        dexpression[i] = DifferentialExpression.cal_de(expression1[i], expression2[i])
##修改G1，G2
    #G1, G2 = readdata.readdata(basename + str(num) + '/' + networkname1, basename + str(num) + '/' + networkname2)
    G1, G2 = readdata.readdata(basename + str(num) + '/' + networkname1)

    # BetweennessCentrality
    data = BetweennessCentrality.cal_bc(G1, G2)
    for x in data:
        vec[int(x) - 1].append(data[x])

    # ClosenessCentrality
    data = ClosenessCentrality.cal_cc(G1, G2)
    for x in data:
        vec[int(x) - 1].append(data[x])

    # ClusteringCoefficient
    data = ClusteringCoefficient.cal_cco(G1, G2)
    for x in data:
        vec[int(x) - 1].append(data[x])

    # DegreeCentrality
    data = DegreeCentrality.cal_dc(G1, G2)
    for x in data:
        vec[int(x) - 1].append(data[x])

    # DifferentialDegreeCentrality
    data = DifferentialDegreeCentrality.cal_ddc(G1, G2)
    for x in data:
        vec[int(x) - 1].append(data[x])

    # DifferentialExpression
    for i in range(0, 100):
        vec[i].append(dexpression[i])

    for x in vec:
        total_vec.append(x)

    # important
    with open(basename + str(num) + '/' + importantname) as file:
        for line in file:
            y[int(line)-1] = 1

    for x in y:
        total_y.append(x)

X = np.array(total_vec)
Y = np.array(total_y)
X_scale = preprocessing.scale(X)
clf = RandomForestClassifier(max_depth=10,n_estimators=100,min_samples_split=5)
clf.fit(X_scale, Y)


#Test
num = 10
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

for i in range(0, 100):
    dexpression[i] = DifferentialExpression.cal_de(expression1[i], expression2[i])

G1, G2 = readdata.readdata(basename + str(num) + '/' + networkname1, basename + str(num) + '/' + networkname2)

# BetweennessCentrality
data = BetweennessCentrality.cal_bc(G1, G2)
for x in data:
    vec[int(x) - 1].append(data[x])

# ClosenessCentrality
data = ClosenessCentrality.cal_cc(G1, G2)
for x in data:
    vec[int(x) - 1].append(data[x])

# ClusteringCoefficient
data = ClusteringCoefficient.cal_cco(G1, G2)
for x in data:
    vec[int(x) - 1].append(data[x])

# DegreeCentrality
data = DegreeCentrality.cal_dc(G1, G2)
for x in data:
    vec[int(x) - 1].append(data[x])

# DifferentialDegreeCentrality
data = DifferentialDegreeCentrality.cal_ddc(G1, G2)
for x in data:
    vec[int(x) - 1].append(data[x])

# DifferentialExpression
for i in range(0, 100):
    vec[i].append(dexpression[i])

Test = np.array(vec)
Test_scale = preprocessing.scale(Test)
result = clf.predict(Test_scale)
for i in range(0,100):
    if (result[i]==1):
        print(i+1)


