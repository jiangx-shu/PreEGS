#!/bin/bash

echo "============开始预处理所有文件============"
rm -f outputRF5.txt
totalTimes=100
for i in $(seq $totalTimes)
do
python3 learn_simu_5features.py $i >> outputRF5.txt
if [ "$?" -ne "0" ];then
echo "$i 执行出错，退出..."
exit 9
fi
done
echo "============预处理完成============"
echo "============开始处理结果=========="

cat outputRF5.txt | awk '{ sum += $1; } END { print "sum = " sum; print "average = " sum/NR }' >> outputRF5result.txt


cat outputRF5.txt | awk '{ sum += $2; } END { print "sum = " sum; print "average = " sum/NR }' >> outputRF5result.txt


cat outputRF5.txt | awk '{ sum += $3; } END { print "sum = " sum; print "average = " sum/NR }' >> outputRF5result.txt


cat outputRF5.txt | awk '{ sum += $4; } END { print "sum = " sum; print "average = " sum/NR }' >> outputRF5result.txt


cat outputRF5.txt | awk '{ sum += $5; } END { print "sum = " sum; print "average = " sum/NR }' >> outputRF5result.txt
