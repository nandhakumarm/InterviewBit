class Solution(object):
    def numSetBits(self,A):
        count=0
        if A==0:
            return 0
        while A>0:
            if A&(A-1)==0:
                return count+1
            else:
                A=A&(A-1)
                count+=1
