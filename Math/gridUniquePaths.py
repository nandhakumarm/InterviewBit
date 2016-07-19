class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        if A==0 or B==0:
            return 0
        import math
        m=A+B-2
        n=A-1
        return math.factorial(m)/(math.factorial(n)*math.factorial(m-n))
