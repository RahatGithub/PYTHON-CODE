# import csv
#
# with open("CSV_FILES/data.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",", quotechar="\"")
#     header = next(csv_reader)
#     rows, data = [], []
#
#     for row in csv_reader:
#         rows.append(row)
#
#     for i in range(99):
#         data.append(dict())
#         for j in range(4):
#             # data[i][header[j]] = rows[i][j]
#             data[i].update({header[j] : rows[i][j]})
#
#     for x in data:
#         print(x)


import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('../Thesis/CSV_FILES/data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    header = next(plots)

    for row in plots:
        x.append(float(row[1]))
        y.append(float(row[3]))


plt.bar(x, y, color='g', width=0.1)
plt.xlabel('Train Loss')
plt.ylabel('Validation Loss')
plt.title('Train Loss vs Validation Loss')
plt.legend()
plt.show()

