class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        low=0
        high=A
        while True:
            mid=(high+low)/2
            if mid*mid==A:
                return mid
            elif (mid+1)*(mid+1)==A:
                return mid+1
            elif mid*mid<A and (mid+1)*(mid+1)>A:
                return mid
            elif mid*mid>A:
                high=mid-1
            elif (mid+1)*(mid+1)<A:
                low=mid+1
