class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        isNeg=False
        if A<0:
            isNeg=True
            A=-1*A
        temp=A
        numRev=0
        while temp>0:
            rem=temp%10
            temp=temp/10
            numRev=numRev*10 + rem
        if isNeg:
            numRev= -numRev
        if numRev < -2147483648 or numRev > 2147483647:
            return 0
        else:
            return numRev 
