class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        myList=list(A)
        leng=len(A)
        #myList[0],myList[leng-1]=myList[leng-1],myList[0]
        for i in range(leng/2):
            myList[i],myList[leng-i-1]=myList[leng-i-1],myList[i]
        return ''.join(myList)

sol=Solution()
print sol.reverseString("((((([{()}[]]{{{[]}}})))))")