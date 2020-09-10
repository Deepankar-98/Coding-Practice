class Solution:
    def nextPermutation(self,A):
        
        i = -1
        j = len(A)-1
        
        for k in reversed(range(len(A))):
            if A[k]>A[k-1]:
                i=k-1
                break
        
        for k in range(len(A)-1,0,-1):
            if A[k]>A[i]:
                j=k
                break
        
        A[i],A[j]=A[j],A[i]
        
        left = i+1
        right = len(A)-1
        
        while(left<right):
            A[left],A[right]=A[right],A[left]
            left+=1
            right-=1
        
        return A