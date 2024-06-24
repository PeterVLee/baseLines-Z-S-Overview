import re
import pandas as pd

def intify(input_list):
    """Turn list elements into ints

    Args:
        input_list (list): List to turn into ints
    """
    for i, line in enumerate(input_list):
        input_list[i] = int(re.findall(r'\d+', line)[0])

def groupify(input_list):
    """Turn list elements into overview.yaml group strs

    Args:
        input_list (list): List to turn into group strs
    """
    for i, line in enumerate(input_list):
        if i == 0:
            input_list[i] = "      - - " + str(line) + "\n"
        else:
            input_list[i] = "        - " + str(line) + "\n"

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