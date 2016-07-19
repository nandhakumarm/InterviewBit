class Solution(object):
    def countAndSay(self,n):
        count=0
        myStr=""
        if n==1:
            return "1"
        if n==2:
            return "11"
        currterm="11"
        currchar=""
        for i in range(3,n+1):
            #print myStr
            myStr=""
            currchar=currterm[0]
            count=1
            for j in range(1,len(currterm)):
                if currterm[j]==currchar:
                    count+=1
                else:
                    myStr+=str(count)+currchar
                    currchar=currterm[j]
                    count=1
            myStr+=str(count)+currchar
            currterm=myStr
        
        currterm=myStr
        return currterm
