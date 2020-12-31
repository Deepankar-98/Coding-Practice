# Using stack
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):           
        stack = []
        count = 0
        for i in A:
            if i == "(":
                stack.append('1')
            else:
                if stack == []:
                    count += 1
                    
                else:
                    stack.pop()
                    
        return count + len(stack)
		
		
# Better Solution without using stack:
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        o=0
        ans=0
        for i in A:
            if(i=='('):
                o+=1
            else:
                if(o>0):
                    o-=1
                else:
                    ans+=1
        return ans+o

