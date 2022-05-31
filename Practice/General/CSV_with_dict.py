import csv

titles = ["Name", "Author", "Publisher", "Price"]

book1 = {"Name" : "Computer Programming", 
         "Author" : "Tamim Shahriar",
         "Publisher" : "Onnorokom",
         "Price" : "250.0"}

book2 = {"Name" : "Machine Learning", 
         "Author" : "Rakibul Hasan",
         "Publisher" : "Dimik",
         "Price" : "295.0"}

book3 = {"Name" : "The Dessert King", 
         "Author" : "Billal Yousuf",
         "Publisher" : "Guardians",
         "Price" : "370.0"}

book_list = [book1, book2, book3]

with open("books.csv", "w") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = titles)
    csv_writer.writeheader()
    csv_writer.writerows(book_list)
    