echo "column 1"
cat outputSVM5.txt | awk '{ sum += $1; } END { print "sum = " sum; print "average = " sum/NR }'
echo "column 2"
cat outputSVM5.txt | awk '{ sum += $2; } END { print "sum = " sum; print "average = " sum/NR }'
echo "column 3"
cat outputSVM5.txt | awk '{ sum += $3; } END { print "sum = " sum; print "average = " sum/NR }'
echo "column 4"
cat outputSVM5.txt | awk '{ sum += $4; } END { print "sum = " sum; print "average = " sum/NR }'
echo "column 5"
cat outputSVM5.txt | awk '{ sum += $5; } END { print "sum = " sum; print "average = " sum/NR }'
