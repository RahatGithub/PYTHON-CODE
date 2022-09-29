import csv

def readCSV(reader):
    for row in reader:
        yield row

# f1 = open('energy_data.csv', 'r')

reader = csv.reader('energy_data.csv') 

print([row for row in readCSV(reader)])


# f2=open("new_data.csv", "w")

# writes = csv.writer(file1,delimiter=' ',quoting=csv.QUOTE_ALL)
# g=mygen(reader)
# for x in g:
#     writes.writerow([x])


# f1.close()