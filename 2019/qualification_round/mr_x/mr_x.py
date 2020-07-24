"""
Written by Lorenzo Vainigli

This program provides a correct solution for the following problem:
https://www.facebook.com/codingcompetitions/hacker-cup/2019/qualification-round/problems/C
"""

import re

filename = "mr_x"
DEBUG = 0

if DEBUG:
    input_filename = filename + "_example_input.txt"
    output_filename = filename + "_example_output.txt"
else:
    input_filename = filename + "_input.txt"
    output_filename = filename + "_output.txt"


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# from https://stackoverflow.com/questions/522372/finding-first-and-last-index-of-some-value-in-a-list-in-python
def find_closepar(expr):
    open_par = expr.index("(")
    i = open_par+1
    skips = 0
    close_par = -1
    while i < len(expr):
        if expr[i] == "(":
            skips = skips + 1
        if expr[i] == ")":
            if skips == 0:
                close_par = i
            else:
                skips = skips - 1
        i = i + 1
    return open_par, close_par



def eval_core(expr, is_x_true):
    if expr == "x":
        return int(is_x_true)
    elif expr == "X":
        return int(not is_x_true)
    elif expr in ["0", "1"]:
        return int(expr)
    elif re.search("^(.)([&|^])(.)$", expr):
        m = re.search("^(.)([&|^])(.)$", expr)
        if m.group(2) == "&":
            return eval_core(m.group(1), is_x_true) and eval_core(m.group(3), is_x_true)
        if m.group(2) == "|":
            return eval_core(m.group(1), is_x_true) or eval_core(m.group(3), is_x_true)
        if m.group(2) == "^":
            return eval_core(m.group(1), is_x_true) ^ eval_core(m.group(3), is_x_true)
    else:
        open_par, close_par = find_closepar(expr)
        return eval_core(expr[:open_par]
                         + str(eval_core(expr[open_par+1:close_par], is_x_true))
                         + expr[close_par+1:], is_x_true)


def eval(expr):
    return eval_core(expr, is_x_true=True)


def eval_neg(expr):
    return eval_core(expr, is_x_true=False)


def solve(expr):
    if eval(expr) == eval_neg(expr):
        # The value of x doesn't affect the result of the expression
        return 0
    else:
        """
        We need to compute the minimum amount of substitution to make the result of the expression independent
        from the value of x. To do that, we start from the top level expression (i.e. the root). 
        If this is a single term expression, we can simply change the x to 1 or 0.
        Otherwise, if is a binary operator we have to go on recursion to find the top-level operator and modify 
        it to make the other ineffective:
        0 with &: 0 and x is always false;
        1 with |: 1 or x is always true.
        The ^ is a little bit complicated: if one of the operands is x, the other must be x or X, so we can have
        x^x = False or X^x = True regardless of the value of x.
        In all cases discussed above, 1 substitution is enough.
        """
        return 1


in_data = []
out_data = []

with open(input_filename, 'r') as fileinput:
    for line in fileinput:
        in_data.append(line.rstrip().split(" "))
fileinput.close()
del in_data[0]

for i in range(len(in_data)):
    out_data.append("Case #" + str(i + 1) + ": " + str(solve(in_data[i][0])))

with open(output_filename, 'w') as fileoutput:
    for line in out_data:
        fileoutput.write(line + "\n")
fileoutput.close()
