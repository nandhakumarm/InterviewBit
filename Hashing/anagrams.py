class Solution(object):
	def anagrams(self,A):
		myDict=dict()
		result=[]
		for i in xrange(len(A)):
			j=''.join(sorted(A[i]))
			if j not in myDict:
				myDict[j]=[]
				myDict[j].append(i+1)
			elif j in myDict:
				myDict[j].append(i+1)
		for k,v in myDict.items():
			result.append(v)
		return result

sol=Solution()
A=["eat", "tea", "tan", "ate", "nat", "bat"]
print sol.anagrams(A)
