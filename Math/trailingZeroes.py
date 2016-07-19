class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        i=1
        sum_zero=0
        while 5**i<=A:
            sum_zero+=A/(5**i)
            i+=1
        return sum_zero
