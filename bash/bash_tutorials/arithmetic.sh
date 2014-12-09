#! /bin/bash

read input
echo "scale = 3;($input)" | bc -l
