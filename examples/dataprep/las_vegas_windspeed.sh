#!/bin/bash

DATA_PATH=$1
if [[ -z "${DATA_PATH}" ]]; then
    DATA_PATH=./
fi;

echo -n "Average wind speed on 2010/04/25 in Las Vegas: "
grep "20100425" ${DATA_PATH}/425247.csv | grep "VEGAS" | cut -d',' -f43 | paste -d+ -s - | awk '{ total += $1; count++ } END { print total/count }'
