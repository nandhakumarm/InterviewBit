class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        count=0
        rem=0
        temp=0
        if A==1:
            return 1
        import math
        for i in xrange(2,int(math.sqrt(A))+1):
            temp=A
            while temp!=1:
                rem=temp%i
                temp=temp/i
                if rem==0 and temp>=i:
                    count+=1
                elif rem!=0:
                    break
                #print temp
            if temp==1 and rem==0:
                #print i,count+1
                return 1
        return 0
