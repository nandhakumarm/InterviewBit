class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
    	B=list(A)
    	for i in range(1,len(A)):
    		A[i]+=A[i-1]
    	maximum=0
    	start=0
    	end=0
    	myDict=dict()
    	for i in range(len(A)):
    		a=A[i]
    		if a==0:
    			#maximum=max(maximum,i+1)
    			if maximum<i+1:
    				maximum=i+1
    				end=i
    			#end=i
    		elif a in myDict:
    			#maximum=max(maximum,i-myDict.get(a))
    			if maximum<i-myDict.get(a):
    				maximum=i-myDict.get(a)
    				start=myDict.get(a)+1
    				end=i

    		else:
    			myDict[a]=i
    	#return maximum,start,end
    	if start==end==0 and B[0]!=0:
    		return None
    	else:
    		return B[start:end+1],start,end,A
sol=Solution()
A=[3,1,0,-1,2]
B=[1 ,2 ,-2 ,4 ,-4]
C=[-19, 8, 2, -8, 19, 5, -2, -5]
print sol.lszero(C)