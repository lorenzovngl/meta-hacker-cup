""""
Written by Lorenzo Vainigli for the Facebook Hacker Cup 2020 Qualification Round
"""

import time

filename = "timber"
DEBUG = True
BIGINPUT = False

if DEBUG:
    if not BIGINPUT:
        input_filename = filename + "_sample_input.txt"
        output_filename = filename + "_sample_output.txt"
    else:
        input_filename = filename + "_sample_biginput.txt"
        output_filename = filename + "_sample_bigoutput.txt"
else:
    input_filename = filename + ".txt"
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


def solve2(P, H):
    print(P, H)
    distances = []
    for i in range(len(P)-1):
        distances.append(abs(P[i]-P[i+1]))
    ground = []
    for i in range(P[0]-H[0], P[-1]+H[-1]+1):
        if i in P:
            ground.append(H[P.index(i)])
        else:
            ground.append('-')
    print(ground)
    #print(distances)
    #for i in range(len(P)):
    #    print("[{}, {}]".format(P[i]-H[i], P[i]))
    #    print("[{}, {}]".format(P[i], P[i]+H[i]))

    D = [[0 for i in range(len(P)+1)] for j in range(len(P)+1)]
    for i in range(len(P)):
        D[i + 1][0] = H[i]
        D[0][i + 1] = H[i]
    for i in range(1, len(P)+1):
        for j in range(1, len(P) + 1):
            """
                        if P[i-1] + H[i-1] == P[j-1] or P[i-1] + H[i-1] == P[j-1] - 1 or \
                                    P[i-1] - H[i-1] == P[j-1] or P[i-1] - H[i-1] == P[j-1] + 1 or \
                                    P[i-1] + H[i-1] == P[j-1] - H[j-1] or P[i-1] - H[i-1] == P[j-1] + H[j-1] or \
                                    P[i-1] + 1 == P[j-1] or P[i-1]-1 == P[j-1]:
                        """
            if P[i-1]+H[i-1] == P[j-1] or P[i-1]-H[i-1] == P[j-1] or P[i-1]+H[i-1] == P[j-1]-H[j-1]:
                D[i][j] = D[i-1][j-1] + H[i-1] - 1
            else:
                D[i][j] = max(D[i - 1][j], D[i][j - 1])
                
    print("\t\t", end='')
    for i in range(len(P)):
        print(i, end='\t')
    print()
    for i in range(len(P)+1):
        if i>0:
            print(i-1, end='\t')
        else:
            print(" ", end='\t')
        for j in range(len(P)+1):
            print(D[i][j], end='\t')
        print()

    return D[-1][-1]

def solve(P, H):
    print(P, H)
    intervals = []
    for i in range(len(P)):
        intervals.append([P[i]-H[i], P[i]])
        intervals.append([P[i], P[i]+H[i]])
        print("[{}, {}]: {}".format(P[i]-H[i], P[i], H[i]))
        print("[{}, {}]: {}".format(P[i], P[i]+H[i], H[i]))
        print(intervals)
    sum = 0
    i = 0
    limit = intervals[0][0]
    while i < len(intervals):
        if intervals[i][0] >= limit:
            sum = sum + intervals[i][1] - intervals[i][0]
            limit = intervals[i][1]
        i = i+1
    return sum


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
    trees = [t for t in in_data[i:i+N]]
    trees.sort(key=lambda x: int(x[0]))
    P = [int(tree[0]) for tree in trees]
    H = [int(tree[1]) for tree in trees]
    out_data.append("Case #" + str(case) + ": " + str(solve2(P, H)))
    i = i + N
    case = case + 1
    if case == 5:
        break

with open(output_filename, 'w') as fileoutput:
    for line in out_data:
        fileoutput.write(line + "\n")
fileoutput.close()

print(execution_time(start_time))
