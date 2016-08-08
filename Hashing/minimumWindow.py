class Solution(object):
    def minWindow(self, s, t):
    	needToFind=[0]*256
    	hasFound=[0]*256
    	for i in range(len(t)):
    		needToFind[ord(t[i])]+=1
    	maxLen=2**32
    	maxBegin=0
    	maxend=0
    	begin=0
    	end=0
    	count=0
    	while begin<len(s) and end<len(s):
    		if needToFind[ord(s[end])]==0:
    			end+=1
    			continue
    		hasFound[ord(s[end])]+=1
    		if hasFound[ord(s[end])]<=needToFind[ord(s[end])]:
    			count+=1
    		if count==len(t):
    			#print maxLen,maxBegin,maxend
    			while needToFind[ord(s[begin])]==0 or hasFound[ord(s[begin])]>needToFind[ord(s[begin])]:
    				if hasFound[ord(s[begin])]>needToFind[ord(s[begin])]:
    					hasFound[ord(s[begin])]-=1
    				begin+=1
    			currLen=end-begin+1
    			if currLen<maxLen:
    				maxLen=currLen
    				maxBegin=begin
    				maxend=end
    		end+=1
    	#print maxLen,maxBegin,maxend,s[maxBegin:maxend+1]
    	if maxLen==2*32:
    		return ""
    	else:
    		return s[maxBegin:maxend+1]

sol=Solution()
#s="ADOBECODEBANC"
#t="ABCG"
s="w"
t="o"
sol.minWindow(s,t)

