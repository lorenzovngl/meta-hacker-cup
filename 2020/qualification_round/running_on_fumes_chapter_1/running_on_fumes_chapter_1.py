""""
Written by Lorenzo Vainigli

This program provides a correct solution for the following problem:
https://www.facebook.com/codingcompetitions/hacker-cup/2020/qualification-round/problems/D1
"""

import time

filename = "running_on_fumes_chapter_1"
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
This solution based on recursion is correct for the sample input, but is very inefficient.
First call: subsolve(0, 1, N, M, M, C)
"""
def subsolve(total_cost, i_city, n_cities, gallons, tank_capacity, refueling_costs):
    if i_city == n_cities:
        # We reach our destination
        return total_cost
    elif gallons == 0:
        # We are forced to refuel
        if C[i_city - 1] == 0:
            # If the current city has no gas station this path is wrong
            return float('inf')
        else:
            # Otherwise we refuel
            return subsolve(total_cost + C[i_city - 1], i_city, n_cities, tank_capacity, tank_capacity, refueling_costs)
    elif gallons == tank_capacity:
        # We exclude refueling beacuse we have the tank full
        return subsolve(total_cost, i_city + 1, n_cities, gallons - 1, tank_capacity, refueling_costs)
    else:
        # To find the optimal solution we need to go on recursion on the two choices:
        # - go to the next city and consume 1 gallon
        # - refuel on the current city if that city has gas station
        go_forward = subsolve(total_cost, i_city + 1, n_cities, gallons - 1, tank_capacity, refueling_costs)
        refueling = subsolve(total_cost + C[i_city - 1], i_city, n_cities, tank_capacity, tank_capacity, refueling_costs)
        if C[i_city - 1] == 0:
            return go_forward
        else:
            return min(go_forward, refueling)

"""
This solution is an iterative version of the previous, but it's still inefficient.
First call: subsolve_iter(0, 1, N, M, M, C)
"""
def subsolve_iter(total_cost, i_city, n_cities, gallons, tank_capacity, refueling_costs):
    stack = [[total_cost, i_city, n_cities, gallons, tank_capacity, refueling_costs]]
    stack_results = []
    print(n_cities)
    calls = 0
    while len(stack) > 0:
        calls = calls + 1
        print(calls)
        params = stack.pop()
        total_cost = params[0]
        i_city = params[1]
        n_cities = params[2]
        gallons = params[3]
        tank_capacity = params[4]
        refueling_costs = params[5]
        if i_city == n_cities:
            # We reach our destination
            stack_results.append(total_cost)
        elif gallons == 0:
            # We are forced to refuel
            if C[i_city - 1] == 0:
                # If the current city has no gas station this path is wrong
                stack_results.append(float('inf'))
            else:
                # Otherwise we refuel
                stack.append([total_cost + C[i_city - 1], i_city, n_cities, tank_capacity, tank_capacity,
                              refueling_costs])
        elif gallons == tank_capacity:
            # We exclude refueling beacuse we have the tank full
            stack.append([total_cost, i_city + 1, n_cities, gallons - 1, tank_capacity, refueling_costs])
        else:
            # To find the optimal solution we need to go on recursion on the two choices:
            # - go to the next city and consume 1 gallon
            # - refuel on the current city if that city has gas station
            if C[i_city-1] == 0:
                stack.append([total_cost, i_city + 1, n_cities, gallons - 1, tank_capacity, refueling_costs])
            else:
                stack.append([total_cost, i_city + 1, n_cities, gallons - 1, tank_capacity, refueling_costs])
                stack.append([total_cost + C[i_city - 1], i_city, n_cities, tank_capacity, tank_capacity, refueling_costs])
    return min(stack_results)


# Following the official solution
def solve(N, M, C):
    # F_i: the minimum cost required to be at city i with a full tank of gas
    # G_i: the minimum cost required to arrive at city i at all (+inf if unachievable)
    L = [{'i': 0, 'F': 0}]
    for i in range(0, N):
        while len(L) > 0 and L[0]['i'] < i - M:
            L.pop(0)
        if len(L) == 0:
            return -1
        if C[i]:
            d = L[0]['F'] + C[i]
            while len(L) > 0 and d <= L[-1]['F']:
                L.pop(-1)
            L.append({'i': i, 'F': d})
    return L[0]['F']


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
    M = int(in_data[i][1])
    i = i + 1
    C = [int(el[0]) for el in in_data[i:i + N]]
    result = solve(N, M, C)
    if result == float('inf'):
        result = -1
    out_data.append("Case #" + str(case) + ": " + str(result))
    i = i + N
    case = case + 1

with open(output_filename, 'w') as fileoutput:
    for line in out_data:
        fileoutput.write(line + "\n")
fileoutput.close()

print(execution_time(start_time))
