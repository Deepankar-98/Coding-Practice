class Solution:
    # @param A : string representing s
    # @param B : integer representing n
    # @return a list of integers
    def findPerm(self, A, B):
        arr = [-1]*B
        
        if A[0]=='I':
            arr[0] = 1
            count = 2
        else:
            count = 1
            
        
        for i in range(-1,-B,-1):
            if A[i] == 'D':
                arr[i]=count
                count+=1
        
        if A[0]=='D':
            arr[0]=count
            count+=1
            
        for i, s in enumerate(A, start=1):
            if s == 'I':
                arr[i]=count
                count+=1
        
        return arr