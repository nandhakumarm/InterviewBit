class Solution(object):
    def lengthOfLastWord(self, A):
        
        length=len(A)
        if length==0:
            return 0
        right=length-1
        #remove spaces from last
        while right>=0 and A[right]==chr(32):
            right-=1
        
        #update string and the length
        A=A[:right+1]
        #print "a"+s+"b"
        length=len(A)
        if length==0:
            return 0
        flag=True
        right=length-1
        while flag and right>=0:
            if A[right]==chr(32):
                flag=False
                break
            else:
                right-=1
        if flag==False:
            return len(A)-(right+1)
        elif flag==True:
            return len(A)-(right+1)
        
