import csv
from collections import deque
with open("documents/data.csv") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    # print(header)
    rows,data = [],[]
    for row in csvreader:
        rows.append(row)

    for i in range(99):
        data.append(dict())
        for j in range(5):
            # data[i].update({header[j] : rows[i][j]})
            data[i][header[j]] = rows[i][j]
    # print(rows[0][1])
    for d in  data:
        print(d)

    print(data)
    with open("documents/name.txt","w") as fi:
        for da in data:
            fi.write(str(da)+'\n')
