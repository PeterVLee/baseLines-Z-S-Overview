import pandas as pd

unsorted_file = 'unsorted.txt'
sorted_file = 'sorted.txt'
list = []

with open(unsorted_file, 'r') as f:
    for line in f:
        list.append(line)

for i, line in enumerate(list):
    list[i] = line[10:-1]
    list[i] = int(list[i])

# sort and remove dupes
list.sort()
nodupes_list = pd.Series(list).drop_duplicates().tolist()

for i, line in enumerate(nodupes_list):
    if i == 0:
        nodupes_list[i] = "      - - " + str(line) + "\n"
    else:
        nodupes_list[i] = "        - " + str(line) + "\n"

with open(sorted_file, 'w') as f:
    for line in nodupes_list:
        f.write(line)
