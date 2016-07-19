class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        power_26=1
        summ=power_26*(ord(A[len(A)-1])-64)
        length=len(A)
        #print summ
        for i in range(length-2,-1,-1):
            power_26*=26
            summ+=(power_26*(ord(A[i])-64))
        return summ
