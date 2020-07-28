"""
Written by Lorenzo Vainigli for the Facebook Hacker Cup 2020 Qualification Round

This program provides a correct solution for the following problem:
https://www.facebook.com/codingcompetitions/hacker-cup/2020/qualification-round/problems/B
"""

import time

filename = "alchemy"
DEBUG = False
BIGINPUT = False
VALIDATION = False

if DEBUG:
    if not BIGINPUT:
        input_filename = filename + "_sample_input.txt"
        output_filename = filename + "_sample_output.txt"
    else:
        input_filename = filename + "_sample_biginput.txt"
        output_filename = filename + "_sample_bigoutput.txt"
elif VALIDATION:
    input_filename = filename + "_validation_input.txt"
    output_filename = filename + "_validation_output.txt"
else:
    input_filename = filename + "_input.txt"
    output_filename = filename + "_output.txt"


def execution_time(start_time):
    finish_time = time.time()
    diff = finish_time - start_time
    min = int(diff/60)
    diff = diff - min*60
    sec = int(diff)
    diff = diff - sec
    ms = round(diff*1000, 3)
    if min > 0:
        return "Execution time: {} min, {} sec, {} ms.".format(min, sec, ms)
    elif sec > 0:
        return "Execution time: {} sec, {} ms.".format(sec, ms)
    else:
        return "Execution time: {} ms.".format(ms)


def solve(N, C):
    # For a given sequence C is possible to forge the Philosopher's Stone only if C contains a number of As and a number
    # of Bs such that the difference between them is exactly 1. This is due to the fact that any reduction leads to
    # remove one A and one B, so if the difference is greater than 1 we finish to have AAA or BBB, otherwise we have
    # two As and one B or two Bs and one A.
    na = C.count('A')
    nb = C.count('B')
    if abs(na-nb) == 1:
        return 'Y'
    else:
        return 'N'


in_data = []
out_data = []
start_time = time.time()

with open(input_filename, 'r') as fileinput:
    for line in fileinput:
        in_data.append(line.rstrip().split(" "))
fileinput.close()
del in_data[0]

i = 0
case = 1
while i < len(in_data):
    print("Case " + str(case))
    N = int(in_data[i][0])
    i = i + 1
    out_data.append("Case #" + str(case) + ": " + str(solve(N, in_data[i][0])))
    i = i + 1
    case = case + 1

with open(output_filename, 'w') as fileoutput:
    for line in out_data:
        fileoutput.write(line + "\n")
fileoutput.close()

print(execution_time(start_time))
