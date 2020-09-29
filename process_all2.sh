#!/bin/bash

echo "============开始预处理所有文件============"
rm -f outputRF4.txt
totalTimes=100
for i in $(seq $totalTimes)
do
python3 learn_simu_4features.py $i >> outputRF4.txt
if [ "$?" -ne "0" ];then
echo "$i 执行出错，退出..."
exit 9
fi
done
echo "============预处理完成============"
echo "============开始处理结果=========="
echo "column 1" >> outputSVM5.txt
cat outputRF4.txt | awk '{ sum += $1; } END { print "sum = " sum; print "average = " sum/NR }' >> outputRF4result.txt

echo "column 2" >> outputSVM5.txt
cat outputRF4.txt | awk '{ sum += $2; } END { print "sum = " sum; print "average = " sum/NR }' >> outputRF4result.txt

echo "column 3" >> outputSVM5.txt
cat outputRF4.txt | awk '{ sum += $3; } END { print "sum = " sum; print "average = " sum/NR }' >> outputRF4result.txt

echo "column 4" >> outputSVM5.txt
cat outputRF4.txt | awk '{ sum += $4; } END { print "sum = " sum; print "average = " sum/NR }' >> outputRF4result.txt

echo "column 5" >> outputSVM5.txt
cat outputRF4.txt | awk '{ sum += $5; } END { print "sum = " sum; print "average = " sum/NR }' >> outputRF4result.txt
