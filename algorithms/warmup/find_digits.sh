#! /bin/bash

read T

for ((l=0;l<T;l++)); do
    read line
    count=0
    for ((c=0;c<${#line};c++)); do
	digit=${line:c:1}
	if ((digit != 0)) && (( line % digit == 0)); then
	    ((count++))
	fi
    done
    echo $count
done
