class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def heapify(self,A):
    	for i in range(len(A)/2,-1,-1):
    		maximum=i
    		if 2*i+1<len(A) and A[maximum]<A[2*i+1]:
    			maximum=2*i+1
    		if 2*i+2<len(A) and A[maximum]<A[2*i+2]:
    			maximum=2*i+2
    		A[i],A[maximum]=A[maximum],A[i]
    	return A
    def insert(self,A,k):
    	A[0]=k
    	i=0
    	while i<len(A):
    		largest=i
    		if 2*i+1<len(A) and A[largest]<A[i*2+1]:
    			largest=2*i+1
    		if 2*i+2<len(A) and A[largest]<A[i*2+2]:
    			largest=2*i+2
    		if largest==i:
    			break
    		else:
    			A[i],A[largest]=A[largest],A[i]
    			i=largest
    	return A

    def kthsmallest(self, A, k):
    	heap=[0]*k
    	for i in range(k):
    		heap[i]=A[i]
    	self.heapify(heap)
    	#print heap
    	for i in range(k,len(A)):
    		if A[i]<=heap[0]:
    			heap=self.insert(heap,A[i])
    	return heap[0]


sol=Solution()
#A=[12, 3, 5, 7, 19,2,8,14,25,6,47,51,19,18,15]
A=[ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
A.sort()
#print A
print sol.kthsmallest(A,11)


