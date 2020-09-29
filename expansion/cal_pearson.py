import math

#计算特征和类的平均值
def calcMean(x,y):
    sum_x = sum(x)
    sum_y = sum(y)
    n = len(x)
    x_mean = float(sum_x+0.0)/n
    y_mean = float(sum_y+0.0)/n
    return x_mean,y_mean

#计算Pearson系数
def calcPearson(x,y):
    x_mean,y_mean = calcMean(x,y)	#计算x,y向量平均值
    n = len(x)
    sumTop = 0.0
    sumBottom = 0.0
    x_pow = 0.0
    y_pow = 0.0
    for i in range(n):
        sumTop += (x[i]-x_mean)*(y[i]-y_mean)
    for i in range(n):
        x_pow += math.pow(x[i]-x_mean,2)
    for i in range(n):
        y_pow += math.pow(y[i]-y_mean,2)
    sumBottom = math.sqrt(x_pow*y_pow)
    p = sumTop/sumBottom
    return p

def sortedDictValues1(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]

vec =  {}
rela = {}
important_gene = set()

# 读入差异信息向量
#with open(r'/Users/jiaxinlee/Desktop/research/realdata2/vec.txt') as file:
with open(r'/Users/Lenovo/Desktop/sun/data-new/real_data/训练网络/vec.txt') as file:
    num = 0
    for line in file:
        data = line[:-2].split(' ')
        vec[num] = []
        for x in data:
            vec[num].append(float(x))
        num+=1

for x in vec:
    rela[x] = {}
for x in vec:
    for y in vec:
        rela[x][y] = calcPearson(vec[x],vec[y])

# 读入关键基因列表
#with open(r'/Users/jiaxinlee/Desktop/research/realdata/important.txt') as file:
with open(r'/Users/Lenovo/Desktop/sun/data-new/real_data/训练网络/important.txt') as file:
    for line in file:
        important_gene.add(int(line[:-1].split(' ')[1]))

print(important_gene)

w = set()
for x in important_gene:
    w.add(x)


count = 0
for x in important_gene:
    data = sorted(rela[x].items(), key=lambda d: d[1],reverse=True)
    print(x,end=': ')
    for y in data:
        if (y[0] not in w and y[1]>0.90):
            w.add(y[0])
            count += 1
            print(y,end=' ')
    print()


print(len(w))

# 输出新的关键基因列表
with open ('./new_important.txt','w') as file:
    for x in w:
        file.write(str(x)+'\n')

