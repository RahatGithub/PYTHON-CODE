# =============================================================================
# def isPowerOf2(num):
#     
#     check = not(num & (num-1))  //if 0 then num can be expressed as power of smthing else 'bhag ekhan theke'
#     
#     // only not(0) == True; otherwise for any n, not(n) == False
#     
#     return check
# =============================================================================


def isPowerOf2(num):
    
    return not(num & (num-1))


n = int(input())

print(isPowerOf2(n))