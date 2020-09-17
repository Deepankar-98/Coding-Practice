class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        l=[]
        
        # It converts all numbers to 32 bit binary strings.
        for i in A:
            l.append('{:032b}'.format(i))
            
        # Stores count    
        c=0
        
        # *l converts to string which is basically a
        # list of characters. Hence zip merges the bits together.
        l=list(zip(*l))
        
        # Main loop for countin
        for i in l:
            a=i.count('0')
            b=len(A) - a
            # 2 is multiplied as ever case is repeated twice.
            c+=(2*a*b)
            
        return (c%1000000007)