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
y1 = []  # for Train Loss
y2 = []  # for Validation Loss

with open('CSV_FILES/data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    header = next(reader)

    for row in reader:
        x.append(float(row[0]))
        y1.append(float(row[1]))
        y2.append(float(row[3]))


# plt.bar(x, y1, color='b', width=0.5)
plt.plot(x, y1, color="b", label="Train Loss")
plt.plot(x, y2, color="r", label="Validation Loss")
plt.xlabel('Epoch')
plt.ylabel('Train Loss/Validation Loss')
plt.title('Train Loss/Validation Loss W.R.T. Epoch')
plt.legend()
plt.show()

