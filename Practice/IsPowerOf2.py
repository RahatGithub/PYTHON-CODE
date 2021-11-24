"""Check if the given number can be expressed as power of 2 (n = 2**x)"""

# ============================================================================================================
# def isPowerOf2(num):
#     
#     if num <= 0: 
#       check = False 
#
#     else: 
#       check = not(num & (num-1))  //if 0 then num can be expressed as power of smthing else 'bhag ekhan theke'
#     
#     // only not(0) == True; otherwise for any n, not(n) == False
#     
#     return check
# ============================================================================================================


def isPowerOf2(num):
    
    if num<=0: return False    # result will be always False for any number smaller than or equals to 0
    
    return not(num & (num-1))  # if not less than 0, then it can check further


n = int(input())

print(isPowerOf2(n))