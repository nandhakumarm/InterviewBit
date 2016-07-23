class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        if len(A)<=1:
            return 0
        myStack=[]
        myDict={'(':')','{':'}','[':']'}
        for i in A:
            if i=='[' or i=='(' or i=='{':
                myStack.append(i)
            elif i==']' or i==')' or i=='}':
                if len(myStack)==0:
                    return 0
                temp=myStack.pop()
                #print i, temp
                if myDict.get(temp)!=i:
                    return 0
        #print len(myStack)
        if len(myStack)==0:
            return 1
        else:
            return 0

sol=Solution()
print sol.isValid("[(")