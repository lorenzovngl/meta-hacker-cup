import time

filename = "template"
DEBUG = True

if DEBUG:
    input_filename = filename + "_example_input.txt"
    output_filename = filename + "_example_output.txt"
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
    ms = int(diff*1000)
    if min > 0:
        return "Execution time: {} min, {} sec, {} ms.".format(min, sec, ms)
    elif sec > 0:
        return "Execution time: {} sec, {} ms.".format(sec, ms)
    else:
        return "Execution time: {} ms.".format(ms)



def solve(data):
    return 1


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

print(execution_time(start_time))