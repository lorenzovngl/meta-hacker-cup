""""
Written by Lorenzo Vainigli

This program provides a correct solution for the following problem:
https://www.facebook.com/codingcompetitions/hacker-cup/2020/qualification-round/problems/C
"""

import time

filename = "timber"
DEBUG = False
BIGINPUT = False

if DEBUG:
    if not BIGINPUT:
        input_filename = filename + "_sample_input.txt"
        output_filename = filename + "_sample_output.txt"
    else:
        input_filename = filename + "_sample_biginput.txt"
        output_filename = filename + "_sample_bigoutput.txt"
else:
    input_filename = filename + "_input.txt"
    output_filename = filename + "_output.txt"


def execution_time(start_time):
    finish_time = time.time()
    diff = finish_time - start_time
    min = int(diff / 60)
    diff = diff - min * 60
    sec = int(diff)
    diff = diff - sec
    ms = round(diff * 1000, 3)
    if min > 0:
        return "Execution time: {} min, {} sec, {} ms.".format(min, sec, ms)
    elif sec > 0:
        return "Execution time: {} sec, {} ms.".format(sec, ms)
    else:
        return "Execution time: {} ms.".format(ms)


"""
@param  trees: int[][]
        The positions and the heights of the trees
"""
def solve(trees):
    # Sorted by position
    trees.sort(key=lambda x: int(x[0]))
    # Let I_p be the maximum length of a combined timber interval whose endpoint are [-p, p] and which
    # consists of trees cut down to the right or to the left.
    I = {}
    for p, h in trees:
        I[p] = 0
        I[p + h] = 0
        I[p - h] = 0
    for p, h in trees:
        I[p + h] = max(I[p + h], I[p] + h)  # Cut down to the right
        I[p] = max(I[p], I[p - h] + h)  # Cut down to the left
    # The solution is the maximum value in I
    max_len = 0
    for i in I:
        if I[i] > max_len:
            max_len = I[i]
    return max_len


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
    trees = [[int(t[0]), int(t[1])] for t in in_data[i:i + N]]
    out_data.append("Case #" + str(case) + ": " + str(solve(trees)))
    i = i + N
    case = case + 1

with open(output_filename, 'w') as fileoutput:
    for line in out_data:
        fileoutput.write(line + "\n")
fileoutput.close()

print(execution_time(start_time))
