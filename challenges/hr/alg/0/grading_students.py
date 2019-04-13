#!/bin/python3
# 20190310

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    
    result = []
    for i in grades:
        if i >= 38:
            if 0 < 5*round(float(i)/5)-i < 3: # key: round with base 5: 5*round(float(i)/5)
                i = 5*round(float(i)/5)
                result.append(i)
            else:
                result.append(i)
        elif i < 38:
            result.append(i)
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()