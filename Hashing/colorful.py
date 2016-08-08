class Solution(object):
	def colorful(self,A):
		myList=list(str(A))
		mySet=set()
		for i in range(1,len(myList)+1):
			for j in range(len(myList)-i+1):
				k=j
				prd=1
				while k<i+j:
					prd*=int(myList[k])
					k+=1
				if prd in mySet:
					return 0
				else:
					mySet.add(prd)
		return 1

sol=Solution()
print sol.colorful(3245)