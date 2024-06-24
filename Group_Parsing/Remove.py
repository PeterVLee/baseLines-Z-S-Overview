import pandas as pd
import os
import group_parsing

current_dir = os.path.dirname(os.path.abspath(__file__))

original_file = current_dir + '\\Remove\\original.txt'
remove_file = current_dir + '\\Remove\\remove.txt'
result_file = current_dir + '\\Remove\\result.txt'

original_list = []
remove_list = []

with open(original_file, 'r') as f:
    for line in f:
        original_list.append(line)

with open(remove_file, 'r') as f:
    for line in f:
        remove_list.append(line)

group_parsing.intify(original_list)
group_parsing.intify(remove_list)

original_set = set(original_list)
remove_set = set(remove_list)

result_list = list(original_set - remove_set)

result_list = group_parsing.sort(result_list)

group_parsing.output(result_list, result_file)