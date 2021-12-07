def minimumSwaps(arr): 
    val_in_pos = dict(enumerate(arr,1)) # storing values with respect to their positions [key = position, val = value in that position]
    pos_of_val = {v:k for k,v in val_in_pos.items()} # storing positions with respect to their values [key = value, val = position of that value]
    count = 0 # counter for counting the number of swaps
    for pos in val_in_pos:
        apparent_val = val_in_pos[pos] # the 'apparent_val' is the current value in the position 'pos'  
        if apparent_val != pos: # if the value is not in its right position : 
            apparent_pos = pos_of_val[pos] # the 'apparent_pos' is the current position where the value of 'pos' is now in the main array
            val_in_pos[apparent_pos] = apparent_val # storing the apprent_val in apparent_pos; 
            pos_of_val[apparent_val] = apparent_pos # storing the apparent_pos in apparent_val; 
            val_in_pos[pos] = pos # as we have modified, the new value in the position 'pos' will be 'pos' - as expected
            pos_of_val[pos] = pos # also, the position of the value 'pos' has become 'pos'. means; now the value of 'pos' is stored in the position 'pos'
            count+=1 # one swapping is done
    return count
        
n = int(input())
arr = list(map(int,input().split()))
print(minimumSwaps(arr))