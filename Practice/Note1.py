"""In Python, when we assign one variable to another, then if we do 
any operation on the first one then it automatically applies
on the second one too. e.g. when we have assigned 'li' to a 
new variable 'new_li', then these two lists colaborate with 
each other. So, sorting 'li' automatically sorted 'new_li'.""" 


li = [4, 7, 6, 1, 3, 5]

new_li = li 

li.sort() #Sorted the old list

#Print 'li' and 'new_li' to see that both lists are sorted


"""To avoid this, we need to assign the old list saying that it 
is a list. like below- """

li = [4, 7, 6, 1, 3, 5]

new_li = list(li)

li.sort() #Sorted the old list

#Print 'li' and 'new_li' to see that only 'li' is sorted