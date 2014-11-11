#!/bin/bash

echo -n "Total Percipitation on 2010/04/25 in Madison (hundredths of an inch): "
grep "20100425" 425248.csv | grep "MADISON" | cut -d',' -f 7 | paste -d+ -s - | bc
