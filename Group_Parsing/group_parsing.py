import re
import pandas as pd

def intify(input_list):
    """Turn list elements into ints

    Args:
        input_list (list): List to turn into ints
    """

    bad_lines = []
    bad_line_count = 0

    for i, line in enumerate(input_list):
        try:
            input_list[i] = int(re.findall(r'\d+', line)[0])
        except IndexError:
            bad_lines.append(i)
            continue

    for index in bad_lines:
        input_list.pop(index - bad_line_count)
        bad_line_count += 1

def groupify(input_list):
    """Turn list elements into overview.yaml group strs

    Args:
        input_list (list): List to turn into group strs
    """
    for i, line in enumerate(input_list):
        input_list[i] = "        - " + str(line) + "\n"
    
    input_list[0] = input_list[0][:6] + '-' + input_list[0][7:]
    input_list[-1] = input_list[-1][:-1]

def sort(input_list):
    """Sort list and remove dupes

    Args:
        input_list (_type_): _description_
    """
    input_list.sort()
    result_list = pd.Series(input_list).drop_duplicates().tolist()
    return result_list

def output(input_list, result_file):
    """Generates final overview yaml group list

    Args:
        input_list (list): List to export
        result_file (string): Output file
    """
    groupify(input_list)
    with open(result_file, 'w') as f:
        for line in input_list:
            f.write(line)