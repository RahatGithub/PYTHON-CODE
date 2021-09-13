def fibonacci():
    n = int(input("Number of terms: "))
    prev=0
    cur=1
    next=1
    i=0;
    while i<n:
        print(cur)
        prev = cur
        cur = next
        next = cur + prev
        i+=1

fibonacci()