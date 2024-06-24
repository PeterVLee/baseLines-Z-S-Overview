import pandas as pd
import os
import group_parsing

current_dir = os.path.dirname(os.path.abspath(__file__))

original_file = current_dir + '\\Combine\\original.txt'
result_file = current_dir + '\\Combine\\result.txt'
original_list = []

with open(original_file, 'r') as f:
    for line in f:
        original_list.append(line)

group_parsing.intify(original_list)

result_list = group_parsing.sort(original_list)

group_parsing.output(result_list, result_file)