import csv
with open("documents/data.csv", newline = '') as file:
    csv_reader = csv.reader(file, delimiter = ' ', quotechar = '|')
    csvreader = csv.reader(file)
    header = next(csvreader)
    # print(header)
    rows,cols = [],[]

    for row in csvreader:
        rows.append(row)
    for i in range(5):
        cols.append([])
        for row in rows:
            cols[i].append(row[i])
    # for col in cols:
    #     print(col)
    # for row in rows:
    #     print(row)
    # print(cols[2])
