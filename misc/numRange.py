class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        sum=0
        index=0
        count=0
        i=0
        while i<len(A):
            if sum+A[i]<=C:
                sum+=A[i]
                i+=1
            else:
                while index!=i and sum>=B:
                    count+=1
                    sum-=A[index]
                    index+=1
                if A[i]<=C:
                    sum=A[i]
                    index=i
                else:
                    sum=0
                    index=i+1
                
                i+=1
        return count
sol=Solution()
A=[10,5,1,0,2]
b=6
c=8
print sol.numRange(A,b,c)
