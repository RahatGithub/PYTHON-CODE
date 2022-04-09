# ***Slicing***
bkash_msg = "Your transaction of BDT.12900 is successfull"
transaction_amount = bkash_msg[24:29]  # slices the string from 24th character to 28th character [order: 24,25,26,27,28]. New value: 12900
rev_transaction_amount = bkash_msg[28:23:-1] # slices the string from 28th character to 24th character in reverse order [order: 28,27,26,25,24]. New value: 00921 


# ***Join***
actions = ['Wake up', 'Go to Shopping', 'Open new order', 'Choose', 'Confirm']
print(" >> ".join(actions)) # str.join(iter) takes an iterable and joins all its elements using the str. Output: Wake up >> Go to Shopping >> Open new order >> Choose >> Confirm


# ***Replace***
name = "Rahat"
print(name.replace("hat","sel")) #replaces 'hat' with 'sel' which converts Rahat into Rasel. But it doesn't modify the variable 'name'. Output: Rasel.


# ***Finding the index of a character or a substring***
txt = "Well, ok then. I welcome them all."
print(txt.index('wel')) #Output: 17
print(txt.find('wel')) #Output: 17
print((txt.lower()).find('wel')) #Output: 2  #Ignoring the case of the string
print((txt.lower()).find('wel', 5, 25)) #Output: 17  #Finds the substring between indices 5-25

"""index() vs find()"""
print(txt.find('RAC'))  #Output: -1  #Returns -1 if it doesn't find the substring
print(txt.index('RAC'))  #Output: ValueError: substring not found   #Returns an error if it doesn't find the substring


# ***Format(Use variables within strings)***
amount = 16000
msg = "Your transaction request of BDT.{transaction_amount} is granted."
msg2 = "You have successfully withdrawn BDT.{withdraw_amount:.2f} from your account."  #Specifying the data type of the variable. Here, withdraw_amount is a float.
print(msg.format(transaction_amount=amount)) #Output: Your transaction request of BDT.16000 is granted.
print(msg2.format(withdraw_amount=amount)) #Output: You have successfully withdrawn BDT.16000.00 from your account.