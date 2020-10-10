class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        c = 1
        r = 0
        l = 0
        h = A
        
        # Creating 2D matrix.
        arr = []
        for i in range(A):
            a = []
            for j in range(A):
                a.append(1)
            arr.append(a)
        
        # Traversing the matrix.
        for n in range(A-1):
            # Horizontal top row.
            for j in range (l+r, h-r):
                arr[r][j] = c
                c += 1
                
            # Vertical right side column.    
            for j in range (l+r+1, h-r-1):
                arr[j][A-r-1] = c
                c += 1   
            
            # Horizontal botttom row.
            for j in range (h-r-1, l+r-1, -1):
                arr[A-r-1][j] = c
                c += 1
            
            # Vertical right side column.    
            for j in range (h-r-2, l+r, -1):
                arr[j][r] = c
                c += 1   
            r += 1

        if A%2!=0:
            arr[A//2][A//2] = A**2 

        return arr  

obj = Solution()
A = 4
print(obj.generateMatrix(A))
