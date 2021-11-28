for t in range(int(input())):
    
	computers, cables = map(int, input().split())
    
	hours, ready = 0, 1
    
	while(cables > ready):
		ready *= 2
		hours += 1
        
	if(computers > ready):
		hours += (computers - ready + cables - 1)//cables
        
	print(hours)