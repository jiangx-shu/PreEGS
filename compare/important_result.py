#!/usr/bin/python
# encoding: utf-8
#
# usage: python <$0> current_index
#
import sys
import csv
if len(sys.argv) != 2 :
    print('error')
    exit(-1)
current_index=sys.argv[1]

# 文件夹base地址
basename = '/Users/jiaminsun/Downloads/paper/jiaxinpaper/codeall/DNARF/data/simulated_data/m3_0.05/rho3_0.1_'
DCloc_result='DCloc_result.csv'
DEC_result='DEC_result.csv'
DiffRank_result='DiffRank_result.csv'
importantname = 'important.txt'


# for num in range(1, 2):
num=current_index
expression1 = []
expression2 = []
expression3 = []

y = []
z=[]
acc1=0
pre1=0
sen1=0
spe1=0
f11=0

acc2=0
pre2=0
sen2=0
spe2=0
f12=0

acc3=0
pre3=0
sen3=0
spe3=0
f13=0

with open(basename + str(num) + '/' + DCloc_result,"r") as file:
    reader=csv.reader(file)
    for line in reader:
        expression1.append(line[0])
with open(basename + str(num) + '/' + DEC_result,"r") as file:
    reader=csv.reader(file)
    for line in reader:
        expression2.append(line[0])
with open(basename + str(num) + '/' + DiffRank_result,"r") as file:
    reader=csv.reader(file)
    for line in reader:
        expression3.append(line[0])

with open(basename + str(num) + '/' + importantname) as file:
    for line in file:
        data = line.split('\n')
        y.append(data[0])
        x=str(int(data[0])-1)
        z.append(x)
tp1=0
fn1=0
tp2=0
fn2=0
tp3=0
fn3=0
nnn=30
ppp=70

for i in range(1, 31):
    if(expression1[i] in y):
        tp1=tp1+1
    else:
        fn1=fn1+1
fp1=nnn-tp1
tn1=ppp-fp1
acc1=(tp1+tn1)/(tp1+tn1+fp1+fn1)
pre1=tp1/(tp1+fp1)
sen1=tp1/(tp1+fn1)
spe1=tn1/(tn1+fn1)
if(tp1==0):
    f11=0
elif(tp1!=0):
    f11=2*pre1*sen1/(pre1+sen1)
print(acc1, end=" ")
print(pre1, end=" ")
print(sen1, end=" ")
print(spe1, end=" ")
print(f11, end=" ")


for i in range(1, 31):
    if(expression2[i] in z):
        tp2=tp2+1
    else:
        fn2=fn2+1
fp2=nnn-tp2
tn2=ppp-fp2
acc2=(tp2+tn2)/(tp2+tn2+fp2+fn2)
pre2=tp2/(tp2+fp2)
sen2=tp2/(tp2+fn2)
spe2=tn2/(tn2+fn2)
if(tp2==0):
    f12=0
elif(tp2!=0):
    f12=2*pre2*sen2/(pre2+sen2)
print(acc2, end=" ")
print(pre2, end=" ")
print(sen2, end=" ")
print(spe2, end=" ")
print(f12, end=" ")

for i in range(1, 31):
    if(expression3[i] in z):
        tp3=tp3+1
    else:
        fn3=fn3+1
fp3=nnn-tp3
tn3=ppp-fp3
acc3=(tp3+tn3)/(tp3+tn3+fp3+fn3)
pre3=tp3/(tp3+fp3)
sen3=tp3/(tp3+fn3)
spe3=tn3/(tn3+fn3)
if(tp3==0):
    f13=0
elif(tp3!=0):
    f13=2*pre3*sen3/(pre3+sen3)
print(acc3, end=" ")
print(pre3, end=" ")
print(sen3, end=" ")
print(spe3, end=" ")
print(f13)
