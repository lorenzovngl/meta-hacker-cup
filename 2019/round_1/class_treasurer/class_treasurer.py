"""
Written by Lorenzo Vainigli

This program provides a correct solution for the following problem:
https://www.facebook.com/codingcompetitions/hacker-cup/2019/round-1/problems/B
"""

import time

filename = "class_treasurer"
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
    ms = int(diff*1000)
    if min > 0:
        return "Execution time: {} min, {} sec, {} ms.".format(min, sec, ms)
    elif sec > 0:
        return "Execution time: {} sec, {} ms.".format(sec, ms)
    else:
        return "Execution time: {} ms.".format(ms)


def who_win(votes, K):
    a = votes.count('A')
    b = votes.count('B')
    if a > b + K:
        return "A"
    elif b > a + K:
        return "B"
    else:
        return "D"


# Following the official solution
def solve(data, K):
    MOD = 1000000007
    cost = [2 for i in range(N)]
    for i in range(1, N):
        cost[i] = (cost[i-1] * 2) % MOD
    d = 0
    res = 0
    for i in range(N - 1, -1, -1):
        if data[i] == "B":
            if d < K:
                d = d + 1
                continue
            res = (res + cost[i]) % MOD
        d = max(d-1, 0)
    return int(res)

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
    K = int(in_data[i][1])
    i = i + 1
    out_data.append("Case #" + str(case) + ": " + str(solve(list(in_data[i][0]), K)))
    i = i + 1
    case = case + 1

with open(output_filename, 'w') as fileoutput:
    for line in out_data:
        fileoutput.write(line + "\n")
fileoutput.close()

print(execution_time(start_time))
