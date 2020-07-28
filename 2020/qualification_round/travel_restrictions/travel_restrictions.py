"""
Written by Lorenzo Vainigli for the Facebook Hacker Cup 2020 Qualification Round

This program provides a correct solution for the following problem:
https://www.facebook.com/codingcompetitions/hacker-cup/2020/qualification-round/problems/A
"""

import time

filename = "travel_restrictions"
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


def solve(N, I, O):
    possible_flights = [['-' for i in range(N)] for j in range(N)]
    for dep in range(N):
        for arr in range(N):
            if dep == arr:
                possible_flights[dep][arr] = 'Y'
            elif abs(arr-dep) == 1:
                if O[dep] == 'N' or I[arr] == 'N':
                    possible_flights[dep][arr] = 'N'
                else:
                    possible_flights[dep][arr] = 'Y'
    for dep in range(N):
        for arr in range(N):
            # To deduce if a flight from dep to arr is possible (when they are not adjacent) is necessary that the
            # chain of airports between them did not have a 'N'
            if possible_flights[dep][arr] == '-':
                start = dep
                end = arr
                if dep < arr:
                    step = 1
                else:
                    step = -1
                string = ''
                for i in range(start, end, step):
                    string = string + possible_flights[i][i+step]
                if not 'N' in string:
                    possible_flights[dep][arr] = 'Y'
                else:
                    possible_flights[dep][arr] = 'N'
    result = ''
    for dep in range(len(possible_flights)):
        result += '\n'
        for arr in range(len(possible_flights[dep])):
            result += str(possible_flights[dep][arr])
    return result


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
    out_data.append("Case #" + str(case) + ": " + str(solve(N, in_data[i][0], in_data[i+1][0])))
    i = i + 2
    case = case + 1

with open(output_filename, 'w') as fileoutput:
    for line in out_data:
        fileoutput.write(line + "\n")
fileoutput.close()

print(execution_time(start_time))
