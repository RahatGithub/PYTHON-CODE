brands = ['Bajaj', 'KTM', 'Hero', 'TVS', 'Yamaha'] 

chars = list(ch for brand in brands for ch in brand)

print(len(chars))