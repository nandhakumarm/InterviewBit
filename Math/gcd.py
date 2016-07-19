class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A==0 and B==0:
            return 0
        elif A==0:
            return B
        elif B==0:
            return A
        rem=-1
        while rem!=0:
            rem=A%B
            A=B
            B=rem
        return A
