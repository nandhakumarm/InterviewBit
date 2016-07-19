class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        low=0
        high=len(A)-1
        mid=0
        index=0
        found=False
        while low<=high:
            mid=(low+high)/2
            #print low,mid,high
            if A[mid]==B:
                #print "1"
                index=mid
                found=True
                #print "4"
                break
            elif A[mid]>B:
                #print "2"
                high=mid-1
            elif A[mid]<B:
                #print "3"
                low=mid+1
            #print "jkl"
        #print found
        if found==False:
            return 0
        #print "After found"
        count=1
        left=index-1
        right=index+1
        while left>=0 and A[left]==B:
            count+=1
            left-=1
        while right<len(A) and A[right]==B:
            count+=1
            right+=1
        return count
