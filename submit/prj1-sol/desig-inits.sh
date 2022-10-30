# !/bin/bash
dir=`dirname $0`
MAIN_FILE="parser.py"

read INPUT;

python3 ${MAIN_FILE} -d parser.py $INPUT;