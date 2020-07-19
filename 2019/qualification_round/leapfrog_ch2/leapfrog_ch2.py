"""
Written by Lorenzo Vainigli

This program provides a correct solution for the following problem:
https://www.facebook.com/codingcompetitions/hacker-cup/2019/qualification-round/problems/B
"""

import math

filename = "leapfrog_ch2"
DEBUG = 0

if DEBUG:
    input_filename = filename + "_example_input.txt"
    output_filename = filename + "_example_output.txt"
else:
    input_filename = filename + "_input.txt"
    output_filename = filename + "_output.txt"

in_data = []
out_data = []


def solve(row):
    row = row[0]
    """
    Because A can leap left or right, only 2 B are sufficient to bring A the the last lilypad and it can be done using
    this set of moves:
        AB.B..
        .BAB..
        .B.BA.
        ..BBA.
        .ABB..
        .AB.B.
        ..BAB.
        ..B.BA
    but this number also need to be less than the length of the lilypads minus 2 in order to leave free the first
    spot (A) and the last spot.
    """
    if len(row) <= 3:
        # If there are 3 spots or less we follow the solution of leapfrog_ch1
        if math.floor(len(row)/2) <= row.count('B') <= len(row) - 2:
            return "Y"
        else:
            return "N"
    else:
        if 2 <= row.count('B') <= len(row) - 2:
            return "Y"
        else:
            return "N"


with open(input_filename, 'r') as fileinput:
    for line in fileinput:
        in_data.append(line.rstrip().split(" "))
fileinput.close()
del in_data[0]

for i in range(len(in_data)):
    out_data.append("Case #" + str(i+1) + ": " + solve(in_data[i]))

with open(output_filename, 'w') as fileoutput:
    for line in out_data:
        fileoutput.write(line + "\n")
fileoutput.close()