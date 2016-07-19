class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        top=0
        bottom=len(A)-1
        left=0
        right=len(A[0])-1
        dire=0
        while left<=right and top<=bottom:
            if dire==0:
                for i in range(left,right+1):
                    result.append(A[top][i])
                dire=1
                top+=1
            elif dire==1:
                for i in range(top,bottom+1):
                    result.append(A[i][right])
                dire=2
                right-=1
            elif dire==2:
                for i in range(right,left-1,-1):
                    result.append(A[bottom][i])
                dire=3
                bottom-=1
            elif dire==3:
                for i in range(bottom,top-1,-1):
                    result.append(A[i][left])
                dire=0
                left+=1
        ## Actual code to populate result
        return result

