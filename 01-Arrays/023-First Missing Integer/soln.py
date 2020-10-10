# Using hashing: O(1) time, O(n) space
class Solution:
    def firstMissingPositive(self, A):
        # Removing negetive numbers
        A = [i for i in A if i >= 0]
		
		# Handling corner cases.
        if A == []:
            return 1
            
        low =min(A)
		if min(A) > 1:
			return 1
			
        high = max(A)
        hash_table = set(A)
        
        for i in range(low, high+2):
            if i not in hash_table:
                return i
				
				
# Method-2: --> O(1) space and time comp.
"""Using sum of natoral numbers:

But in this problem it wont work as there might be more than 1 numbers missing and numbers might get repeated.
"""


# Method 3: This method uses the technique of XOR to solve the problem. 
"""Approach: 
XOR has certain properties 
Assume a1 ^ a2 ^ a3 ^ …^ a(n) = a 
and a1 ^ a2 ^ a3 ^ …^ a(n-1) = b

Then a ^ b = a(n)

Algorithm: 
1. Create two variables a = 0 and b = 0
2. Run a loop from 1 to n with i as counter.
3. For every index update a as a = a ^ i
4. Now traverse the array from start to end.
5. For every index update b as b = b ^ array[i]
6. Print the missing number as a ^ b.
"""

# Wrong Solution. 
# As there might be more than 1 no: missing and no: might get repeated.
def getMissingNo(a, n):
    x1 = a[0]
    x2 = 1
     
    for i in range(1, n):
        x1 = x1 ^ a[i]
         
    for i in range(2, n + 2):
        x2 = x2 ^ i
     
    return x1 ^ x2


# Method 4: Best solution and it always works...
class Solution:
    def firstMissingPositive(self, A):
        # Removing negetive numbers.
        A = list(filter(lambda x : x > 0, A))
        
        # A[0] = len(A)+2
        A = [len(A) + 2] + A
        
        # If the traversed element is a valid index then make the 
        # index represented by the element negetive to show that the element is present.
        # And while selecting new element find the absolute value of the element biz 
        # it might be -ve biz that index elemt was found before.
        for i, num in enumerate(A):
            num = abs(num)
            if num < len(A):
                A[num] = (-1) * abs(A[num])
                
        for i in range(1, len(A)):
            j=A[i]
            if j > 0:
                return i
                
        return len(A)

a = Solution()
s = [3,5,4,-1,1,8,14]
print(a.firstMissingPositive(s))

