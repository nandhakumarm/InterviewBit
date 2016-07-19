class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        if A==0:
            return "0"
        myList=[]
        while A>0:
            myList.append(str(A%2))
            A=A/2
        myList.reverse()
        return "".join(myList)
                

