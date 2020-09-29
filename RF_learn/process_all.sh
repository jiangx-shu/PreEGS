#!/bin/bash

echo "============开始预处理所有文件============"
rm -f output.txt
totalTimes=100
for i in $(seq $totalTimes)
do
  python3 learn_simu_4features.py $i >> output.txt
  wait
done
echo "============预处理完成============"
