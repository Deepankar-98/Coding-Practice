class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        n = len(A)
        a = float(A[0])
        b = float(A[1])
        c = float(A[2])

        for i in range(3 , n):
            if ((a+b+c) > 1 and (a+b+c) < 2):
                return 1

            elif ((a+b+c) > 2):
                # Replace the max element with i'th element
                if (a>b and a>c):
                    a = float(A[i])
                elif (b>a and b>c):
                    b = float(A[i])
                elif (c>a and c>b):
                    c = float(A[i])

            else:
                # Replace the min element with i'th element
                if (a<b and a<c):
                    a = float(A[i])
                elif (b<a and b<c):
                    b = float(A[i])
                elif (c<a and c<b):
                    c = float(A[i])

        # If the ending values satisfy the condition.            
        if ((a+b+c) > 1 and (a+b+c) < 2) :
            return 1
        else:
            return 0


