#!/bin/bash
# Gets list of files on s3

aws s3 ls s3://prime-numbers-buck123/
# 2023-04-05 12:40:28        127 prime_numbers_short.txt

# alternative
#aws s3api list-objects --bucket prime-numbers-buck123 --query 'Contents[].{Key: Key}'

# determine file name
FILENAME=$(aws s3 ls s3://prime-numbers-buck123/ | awk '{print $4}')


# run detect_prime_numbers.py
python3 detect_prime_numbers.py $FILENAME