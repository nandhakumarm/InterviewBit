class Solution(object):
    def prevSmaller(self,A):
        myStack=[]
        finArray=[]
        for i in range(len(A)):
            while len(myStack)!=0 and myStack[-1]>=A[i]:
                myStack.pop()
            if len(myStack)==0:
                finArray.append(-1)
            else:
                finArray.append(myStack[-1])
            myStack.append(A[i])
        return finArray

sol=Solution()
A=[1, 6, 4, 10, 0, 5]
B=[39, 27, 11, 4, 24, 32, 32, 1]
print sol.prevSmaller(A)
print sol.prevSmaller(B)