class Solution(object):
    def isValid(self,s):
        if s[0]=="0":
            if s=="0":
                return True
            else:
                return False
        if int(s)<=255 and int(s)>=0:
            return True
        return False
    def restoreIpAddresses(self,s):
        leng=len(s)
        if leng<4 or leng>12:
            return []
        myList=[]
        for i in range(0,3):
            if i<leng:
                if Solution.isValid(self,s[:i+1]):
                    for j in range(i+1,i+4):
                        if j<len:
                            if Solution.isValid(self,s[i+1:j+1]):
                                for k in range(j+1,j+4):
                                    if k<len:
                                        #print i,j,k
                                        if k+1<leng and Solution.isValid(self,s[j+1:k+1]) and Solution.isValid(self,s[k+1:]):
                                            temp=s[:(i+1)]+"."+s[(i+1):(j+1)]+"."+s[(j+1):(k+1)]+"."+s[(k+1):]
                                            myList.append(temp)
    
        return myList
