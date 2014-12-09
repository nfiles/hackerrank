#! /bin/bash

while read line; do
    echo $(echo $line | cut -c2)
done
