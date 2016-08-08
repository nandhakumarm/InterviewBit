class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        end=0
        myStr=""
        maxLen=0
        i=0
        while i<len(s) and end<len(s) and start<len(s):
            if myStr.rfind(s[i])==-1:
                myStr+=s[i]
                i+=1
                end+=1
                #print myStr
            else:
                if maxLen<(len(myStr)):
                    maxLen=(len(myStr))
                start=myStr.rfind(s[i])+1
                #print start
                end=start
                #i=i+1
                myStr=myStr[start:]   #print maxLen
        if maxLen<(len(myStr)):
            maxLen=(len(myStr))
                #start=i+1
        return maxLen
sol=Solution()
print sol.lengthOfLongestSubstring("bbb")