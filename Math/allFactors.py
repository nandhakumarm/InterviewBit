class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        myList=[]
        import math
        if A==1:
            myList.append(1)
            return myList
        for i in range(1,int(math.sqrt(A))+1):
            if A%i==0:
                myList.append(i)
                if A/i!=i:
                    myList.append(A/i)
        #myList.append(A)
        return sorted(myList)

