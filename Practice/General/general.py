import time

init1 = time.time()
x = 0
for i in range(1, 100001): x+=1
time.sleep(1)
final1 = time.time()
print(f"Total time for FOR loop: {final1-init1}")

init2 = time.time()
x = 0
i = 0
while i < 100000:
    x+=1
    i+=1
final2 = time.time()
print(f"Total time for WHILE loop: {final2-init2}")