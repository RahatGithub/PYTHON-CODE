"""HOW TO WRITE IN A CSV FILE"""

import csv

titles = ["Product Code", "Product Name", "Price", "Seller"]

prd1 = ["20114521", "Garnier Face wash", "490", "Manikpur Store"]

prd2 = ["20114691", "Lionbeard beard oil", "340", "Biharilal Store"]

prd3 = ["20418521", "All clear shampoo", "210", "MBM Store"]

prd_list = [prd1, prd2, prd3]


with open("products.csv", "w") as csv_file:

    csv_writer = csv.writer(csv_file, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
    
    csv_writer.writerow(titles)
    
    csv_writer.writerows(prd_list)


# =============================================================================

# HOW TO READ FROM A CSV FILE

# import csv
# 
# with open("products.csv", newline = '') as csv_file:
#     
#     csv_reader = csv.reader(csv_file, delimiter = ' ', quotechar = '|')
#     
#     for row in csv_reader:
#         
#         print(', '.join(row))
# =============================================================================
