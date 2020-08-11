 # Kadane's Algorithm: Also handles case containing all -ve numbers 
 def maxSubArray(A):
    cs=0   # Current Sum
    ms=0    # Max Sum

    for i in A:
        if cs + i < 0:
            cs = 0
            
        else:
            cs += i
                
            if cs > ms:
                ms = cs

    if ms == 0:
        return max(A)
    return ms


maxSubArray([1,2,3,4])