class Solution(object):
    def braces(self, A):
        if len(A)==0:
            return 0
        myStack=[]
        ctr=0
        for i in range(len(A)):
            if A[i]!=')':
                myStack.append(A[i])
            else:
                ctr=0
                while myStack[-1]!='(':
                    myStack.pop()
                    ctr+=1
                myStack.pop()
                if ctr==0 or ctr==1:
                    return 1
        return 0

A=""
sol=Solution()
print sol.braces(A)