from queue import Queue 

Q = Queue(maxsize=3)   # Declaring a Queue named 'Q' whose maximum size is 3. It is also possible not to set the maxsize

Q.put("Joynal")        # Put/enqueue value in Q 

Q.put("Sayem")         

Q.put("Rakib")

Q.put_nowait("Saimum") # This will throw an error as the Queue is full and we're trying to put a value. 
                       # If we use Q.put(), then it won't throw an error but the program won't work properly

Q.get()                # Get/dequeue value from Q. Output : "Joynal"

Q.get()                # Get/dequeue value from Q. Output : "Sayem"

Q.get()                # Get/dequeue value from Q. Output : "Rakib"

Q.get_nowait()         # This will throw an error as the Queue is empty and we're trying to get a value. 
                       # If we use Q.get(), then it won't throw an error but the program won't work properly

Q.empty()              # Checking if the Queue is empty. Output : True //qsize == 0

Q.put("Akash")

Q.put("Leo")

Q.put("Jeniffer")

Q.qsize()              # The size of the Queue. Output : 3

Q.full()               # Checking if the Queue is full. Output : True //maxsize == qsize

Q.maxsize              # The maximum size that is set. Output : 3

Q.maxsize = 5          # Updating the maximum size

Q.maxsize              # Output : 5