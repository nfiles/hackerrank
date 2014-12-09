#! /bin/bash

read N

total=0
for ((c=0;c<N;c++)); do
    read num
    total=$(expr $total + $num)
done

echo "scale=3; $total / $N" | bc -l
