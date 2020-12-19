class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    
    def search(self, A, B):
        
        # Finding Pivot;
        n=len(A)
        l, h = 0, n-1
        pivot = 0
        while l <= h:
            mid = (l+h)//2

            # Checking if we get the search element
            if A[mid] == B:
                return mid

            # Pivot finding operation
            if A[mid-1] > A[mid]:
                pivot = mid
                break
            elif A[mid] >= A[0]:
                l=mid+1
            else:
                h=mid-1
        
        # Checking search range
        if B < A[pivot] or B > A[pivot-1]:
            return -1

        # Check which half the element lies in.
        if B >= A[0]:
            l=0
            h=mid-1
        else:
            l=mid
            h=n-1

        # Normal Binary Search
        while l <= h:
            mid = (l+h)//2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                l=mid+1
            else:
                h=mid-1

        # print(pivot)
        # print(A)
        return -1