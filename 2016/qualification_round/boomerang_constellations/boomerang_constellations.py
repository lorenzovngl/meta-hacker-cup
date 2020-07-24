"""
Written by Lorenzo Vainigli

This program provides a correct solution for the following problem:
https://www.facebook.com/codingcompetitions/hacker-cup/2016/qualification-round/problems/A
"""

import time
from math import sqrt, pow

filename = "boomerang_constellations"
DEBUG = False

if DEBUG:
    input_filename = filename + "_sample_input.txt"
    output_filename = filename + "_sample_output.txt"
else:
    input_filename = filename + "_input.txt"
    output_filename = filename + "_output.txt"


def distance(p1, p2):
    # The distance between p1=(x1,y1) and p2=(x2,y2) is sqrt((x2-x1)^2+(y2-y1)^2)
    return sqrt(pow(int(p2[0])-int(p1[0]), 2) + pow(int(p2[1])-int(p1[1]), 2))


# Following the official solution:
# https://www.facebook.com/notes/1264355396913692
def solve(stars):
    constellations = 0
    for star in stars:
        other_stars = [el for el in stars if el != star]
        distances = [distance(star, el) for el in other_stars]
        distances.sort()
        grouped_distances = {}
        for d in distances:
            if d not in grouped_distances:
                grouped_distances[d] = 0
            grouped_distances[d] = grouped_distances[d] + 1
        acc = 0
        for d in grouped_distances:
            x = grouped_distances[d]
            acc = acc + (x*(x-1)/2)
        constellations = constellations + acc
    return int(constellations)


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
    out_data.append("Case #" + str(case) + ": " + str(solve(in_data[i:i+N])))
    i = i + N
    case = case + 1

with open(output_filename, 'w') as fileoutput:
    for line in out_data:
        fileoutput.write(line + "\n")
fileoutput.close()

print("Execution time: %s seconds." % (time.time() - start_time))
