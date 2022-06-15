import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('CSV_FILES/data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    header = next(reader)

    for row in reader:
        x.append(float(row[1]))
        y.append(float(row[3]))


plt.plot(x, y, color='g')
plt.xlabel('Train Loss')
plt.ylabel('Validation Loss')
plt.title('Train Loss vs Validation Loss')
plt.legend()
plt.show()