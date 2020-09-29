from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn import preprocessing
from read import readdara_real
from sklearn.linear_model import LogisticRegression
from features import DifferentialExpression
from features import BetweennessCentrality
from features import DegreeCentrality
from features import ClosenessCentrality
from features import ClusteringCoefficient
from features import DifferentialDegreeCentrality

record = []
for i in range(0, 247):
    record.append(0)

for turns in range(0,100):
    print('turns:',turns)
    # 准备训练集
    expression1 = []
    expression2 = []
    dexpression = []
    vec = []
    y = []


    for i in range(0, 486):
        dexpression.append(0)
        vec.append([])
        y.append(0)

    # NHA基因表达向量
    with open(r'/Users/Lenovo/Desktop/sun/code/RF_learn/real_data/训练网络/nha_gene_vec.txt') as file:
        for line in file:
            data = line[:-2].split(' ')
            expression1.append(data)

    E1 = preprocessing.scale(np.array(expression1))
    expression1 = E1.tolist()

    # SKNSH基因表达向量
    with open(r'/Users/Lenovo/Desktop/sun/code/RF_learn/real_data/训练网络/sknsh_gene_vec.txt') as file:
        for line in file:
            data = line[:-2].split(' ')
            expression2.append(data)

    E2 = preprocessing.scale(np.array(expression2))
    expression2 = E2.tolist()

    for i in range(0, 486):
        dexpression[i] = DifferentialExpression.cal_de(expression1[i], expression2[i])

    # 读NHA和SKNSH网络数据
    G1, G2 = readdara_real.readdata(r'/Users/Lenovo/Desktop/sun/code/RF_learn/real_data/训练网络/nhaedges.txt',
                                    r'/Users/Lenovo/Desktop/sun/code/RF_learn/real_data/训练网络/sknshedges.txt')

    # BetweennessCentrality
    w = []
    for i in range(0, 486):
        w.append(0)
    data = BetweennessCentrality.cal_bc(G1, G2)
    for x in data:
        w[int(x)] = 1
        vec[int(x)].append(data[x])
    for i in range(0, 486):
        if (w[i] == 0):
            vec[i].append(0)

    # ClosenessCentrality
    w = []
    for i in range(0, 486):
        w.append(0)
    data = ClosenessCentrality.cal_cc(G1, G2)
    for x in data:
        w[int(x)] = 1
        vec[int(x)].append(data[x])
    for i in range(0, 486):
        if (w[i] == 0):
            vec[i].append(0)

    # ClusteringCoefficient
    w = []
    for i in range(0, 486):
        w.append(0)
    data = ClusteringCoefficient.cal_cco(G1, G2)
    for x in data:
        w[int(x)] = 1
        vec[int(x)].append(data[x])
    for i in range(0, 486):
        if (w[i] == 0):
            vec[i].append(0)

    # DegreeCentrality
    w = []
    for i in range(0, 486):
        w.append(0)
    data = DegreeCentrality.cal_dc(G1, G2)
    for x in data:
        w[int(x)] = 1
        vec[int(x)].append(data[x])
    for i in range(0, 486):
        if (w[i] == 0):
            vec[i].append(0)

    # DifferentialDegreeCentrality
    w = []
    for i in range(0, 486):
        w.append(0)
    data = DifferentialDegreeCentrality.cal_ddc(G1, G2)
    for x in data:
        w[int(x)] = 1
        vec[int(x)].append(data[x])
    for i in range(0, 486):
        if (w[i] == 0):
            vec[i].append(0)

    # DifferentialExpression
    for i in range(0, 486):
        vec[i].append(dexpression[i])

    # important
    with open(r'/Users/Lenovo/Desktop/sun/code/RF_learn/real_data/训练网络/new_important.txt') as file:
        for line in file:
            y[int(line[:-1])] = 1

    print(y)


    # 训练模型
    X = np.array(vec)
    Y = np.array(y)
    X_scale = preprocessing.scale(X)
    # 将向量输出
    with open(r'/Users/Lenovo/Desktop/sun/code/RF_learn/real_data/训练网络/vec.txt','w') as file:
        for x in X_scale:
            for y in x:
                file.write(str(y)+' ')
            file.write('\n')
    #clf = LogisticRegression(n_estimators=100)
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_scale, Y)


    # 准备测试集

    expression1 = []
    expression2 = []
    dexpression = []
    vec = []
    y = []


    for i in range(0, 247):
        dexpression.append(0)
        vec.append([])
        y.append(0)

    # 读NB4基因表达向量
    with open(r'/Users/Lenovo/Desktop/sun/code/RF_learn/real_data/测试网络/NB4_genevec.txt') as file:
        for line in file:
            data = line[:-2].split(' ')
            expression1.append(data)

    E1 = preprocessing.scale(np.array(expression1))
    expression1 = E1.tolist()

    # 读HMVEC_dBlAd基因表达向量
    with open(r'/Users/Lenovo/Desktop/sun/code/RF_learn/real_data/测试网络/HMVEC_dBlAd_genevec.txt') as file:
        for line in file:
            data = line[:-2].split(' ')
            expression2.append(data)

    E2 = preprocessing.scale(np.array(expression2))
    expression2 = E2.tolist()

    for i in range(0, 247):
        dexpression[i] = DifferentialExpression.cal_de(expression1[i], expression2[i])

    # 读NB4和HMVEC_dBlAd网络数据
    G1, G2 = readdara_real.readdata(r'/Users/Lenovo/Desktop/sun/code/RF_learn/real_data/测试网络/NB4_edgelist.txt',
                                    r'/Users/Lenovo/Desktop/sun/code/RF_learn/real_data/测试网络/HMVEC_dBlAd_edgelist.txt')

    # BetweennessCentrality
    w = []
    for i in range(0, 247):
        w.append(0)
    data = BetweennessCentrality.cal_bc(G1, G2)
    for x in data:
        w[int(x)] = 1
        vec[int(x)].append(data[x])
    for i in range(0, 247):
        if (w[i] == 0):
            vec[i].append(0)

    # ClosenessCentrality
    w = []
    for i in range(0, 247):
        w.append(0)
    data = ClosenessCentrality.cal_cc(G1, G2)
    for x in data:
        w[int(x)] = 1
        vec[int(x)].append(data[x])
    for i in range(0, 247):
        if (w[i] == 0):
            vec[i].append(0)

    # ClusteringCoefficient
    w = []
    for i in range(0, 247):
        w.append(0)
    data = ClusteringCoefficient.cal_cco(G1, G2)
    for x in data:
        w[int(x)] = 1
        vec[int(x)].append(data[x])
    for i in range(0, 247):
        if (w[i] == 0):
            vec[i].append(0)

    # DegreeCentrality
    w = []
    for i in range(0, 247):
        w.append(0)
    data = DegreeCentrality.cal_dc(G1, G2)
    for x in data:
        w[int(x)] = 1
        vec[int(x)].append(data[x])
    for i in range(0, 247):
        if (w[i] == 0):
            vec[i].append(0)

    # DifferentialDegreeCentrality
    w = []
    for i in range(0, 247):
        w.append(0)
    data = DifferentialDegreeCentrality.cal_ddc(G1, G2)
    for x in data:
        w[int(x)] = 1
        vec[int(x)].append(data[x])
    for i in range(0, 247):
        if (w[i] == 0):
            vec[i].append(0)

    # DifferentialExpression
    for i in range(0, 247):
        vec[i].append(dexpression[i])

    X = np.array(vec)
    X_scale = preprocessing.scale(X)
    # 预测
    result = clf.predict(X_scale)
    print(result)
    cnt = 0
    for x in result:
        if x == 1:
            print(cnt)
            record[cnt]+=1
        cnt+=1

print('++++++++++++++++++++++')
for i in range(0, 247):
    if (record[i]!=0):
        print(i,record[i])


'''
Result:
33 7 
71 100
78 100
87 4
99 24
117 3
123 11
127 1
128 1
131 100
146 100
157 1
160 1
171 3
172 23
174 5
178 1
185 24
201 97
219 19
229 14
232 13
246 3
'''
'''
2 2
33 8
41 1
45 1
71 100
78 97
87 1
92 3
94 1
99 15
114 1
117 3
123 15
128 1
131 98
138 2
141 1
145 1
146 100
157 1
171 6
172 19
174 2
175 1
178 2
180 1
185 28
201 97
219 22
229 10
232 7
234 1
'''