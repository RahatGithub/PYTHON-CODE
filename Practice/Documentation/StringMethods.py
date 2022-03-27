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