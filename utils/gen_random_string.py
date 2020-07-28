import sys
import random


# From https://pynative.com/python-generate-random-string/
def get_random_string(letters, length):
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(result_str)


get_random_string(sys.argv[1], int(sys.argv[2]))