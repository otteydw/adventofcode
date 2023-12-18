#!/bin/bash

TEMPLATE_DIRECTORY=~/git/adventofcode/template

DAY_NUMBER=$1
NEW_DAY="day${DAY_NUMBER}"

cp -a ${TEMPLATE_DIRECTORY} ${NEW_DAY}

cd ${NEW_DAY}

gsed -e "s|dayXX|${NEW_DAY}|g" -i *.py

mv dayXX.py ${NEW_DAY}.py
mv test_dayXX.py test_${NEW_DAY}.py
