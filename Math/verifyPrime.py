class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A==1:
            return 0
        import math
        root_A=int(math.sqrt(A))
        for i in range(2,root_A+1):
            if A%i==0:
                return 0
        return 1

