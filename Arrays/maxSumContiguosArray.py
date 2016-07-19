class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_sum=0
        max_till_current=0
        if max(A)<0:
            max_sum=max(A)
        else:
            for i in A:
                max_till_current+=i
                if max_till_current<0:
                    max_till_current=0
                if max_sum<max_till_current:
                    max_sum=max_till_current
        return max_sum

