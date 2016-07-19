class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        size=len(A)
        for i in range(0,size/2):
            for j in range(i,size-1-i):
                temp=A[i][j]
                A[i][j]=A[size-j-1][i]
                A[size-j-1][i]=A[size-i-1][size-j-1]
                A[size-i-1][size-j-1]=A[j][size-i-1]
                A[j][size-i-1]=temp
        return A
