class Solution:
    # @param A : integer
    # @return a list of integers
    def test(self,A):
        print A
    def isPrime(self, A):
        if A==1:
            return 0
        import math
        root_A=int(math.sqrt(A))
        for i in xrange(2,root_A+1):
            if A%i==0:
                return 0
        return 1
    def primesum(self, A):
        for i in xrange(2,A+1):
            if Solution.isPrime(self, i)==1:
                temp=A-i
                if Solution.isPrime(self, temp)==1:
                    return [i,temp]
