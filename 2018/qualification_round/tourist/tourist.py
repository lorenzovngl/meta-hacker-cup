"""
Written by Lorenzo Vainigli

This program provides a correct solution for the following problem:
https://www.facebook.com/codingcompetitions/hacker-cup/2018/qualification-round/problems/A
"""

from functools import cmp_to_key

filename = "tourist"
DEBUG = 0

if DEBUG:
    input_filename = filename + "_example_input.txt"
    output_filename = filename + "_example_output.txt"
else:
    input_filename = filename + "_input.txt"
    output_filename = filename + "_output.txt"


def compare(a, b):
    if a['visits'] == b['visits']:
        if a['popularity'] < b['popularity']:
            return 1       # Reverse order
        elif a['popularity'] > b['popularity']:
            return -1      # Reverse order
        else:
            return 0
    elif a['visits'] < b['visits']:
        return -1
    elif a['visits'] > b['visits']:
        return 1


# The following is a bad solution because we tell to the program to exactly what
# the problem statement say. Usually this type of solution for FHC problems is
# too easy and the program may have a large complexity in time.
def solve_bad(K, V, attractions):
    print(K, V)
    attractions = [{'visits': 0, 'popularity': len(attractions)-i, 'name': item}
                   for (i, sublist) in enumerate(attractions)
                   for item in sublist]
    print(attractions)
    # For each visit
    print(V)
    for v in range(V):

        # Sort the places first by number of visits (ascending) and then by popularity (descending)
        attractions = sorted(attractions, key=cmp_to_key(compare))

        # Visit the first K attractions
        for k in range(K):
            attractions[k]['visits'] = attractions[k]['visits'] + 1

    for att in attractions:
        print(att['name'], att['visits'], att['popularity'])

    return ' '.join([attr['name'] for attr in attractions[:K]])


# To find the correct solution we must observe that reordering the items in the
# array of attractions is useless: the order changes but in a circular way, so
# we can use array indexes rather than physically ordering the items.
def solve(K, V, attractions):
    attractions = [item for sublist in attractions for item in sublist]

    if len(attractions) > V:
        start = ((V-1)*K) % len(attractions)
        end = start+K
    else:
        start = len(attractions) % ((V-1)*K)-1
        end = start+K

    circular = 0
    if end > len(attractions):
        end = end - len(attractions)
        circular = 1

    if not circular:
        return ' '.join(attractions[start:end])
    else:
        return ' '.join(attractions[:end]+attractions[start:])


in_data = []
out_data = []

with open(input_filename, 'r') as fileinput:
    for line in fileinput:
        in_data.append(line.rstrip().split(" "))
fileinput.close()
del in_data[0]

i = 0
case = 1
while i < len(in_data):
    N = int(in_data[i][0])      # Number of attractions
    K = int(in_data[i][1])      # Number of attractions Alex wants to see
    V = int(in_data[i][2])      # The ordinal number of the visit
    attractions = in_data[i+1:i+1+N]
    out_data.append("Case #" + str(case) + ": " + str(solve(K, V, attractions)))
    i = i+1+N
    case = case + 1

with open(output_filename, 'w') as fileoutput:
    for line in out_data:
        fileoutput.write(line + "\n")
fileoutput.close()
