class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        length=len(A)
        for i in xrange(length):
            A[i]+=(A[A[i]]%length)*length
        for i in xrange(length):
            A[i]=A[i]/length
