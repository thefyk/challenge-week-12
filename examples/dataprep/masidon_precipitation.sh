#!/bin/bash

DATA_PATH=$1
if [[ -z "${DATA_PATH}" ]]; then
    DATA_PATH=./
fi;

echo -n "Total Percipitation on 2010/04/25 in Madison (hundredths of an inch): "
grep "20100425" ${DATA_PATH}/425248.csv | grep "MADISON" | cut -d',' -f 7 | paste -d+ -s - | bc
