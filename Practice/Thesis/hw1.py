import csv
from collections import deque
with open("documents/data.csv", newline = '') as file:
    csv_reader = csv.reader(file, delimiter = ' ', quotechar = '|')
    csvreader = csv.reader(file)
    header = next(csvreader)
    # print(header)
    rows,cols = deque([]),deque([])
    data = dict()
    for row in csvreader:
        rows.append(row)
    for i in range(5):
        cols.append([])
        for row in rows:
            cols[i].append(row[i])

    for col in cols:
        col =[float(x) for x in col]
        print(sum(col))
    print()
    # print(type(cols), type(cols[0]))
    # su = cols[2]+cols[1]
    # for s in su:
    #     print(s)

