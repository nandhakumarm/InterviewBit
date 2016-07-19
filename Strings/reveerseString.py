class Solution(object):
    def reverseWords(self,A):
        length=len(A)
        if length==0:
            return 0
        right=length-1
        #remove spaces from last
        while right>=0 and A[right]==chr(32):
            right-=1
        #update string and the length
        A=A[:right+1]
        length=len(A)
        left=0
	
	#remove spaces from last
        while left<length and A[left]==chr(32):
            left+=1
        A=A[left:]
        length=len(A)
        if length==0:
            return 0
        #flag=True
        right=length-1
        temp=[]
        #print temp,right
        while right>=0:
            #print temp,right
            if A[right]==chr(32):
                #print "1"
                temp.append(A[right+1:])
                A=A[:right+1]
                right2=len(A)-1
        #remove spaces from last
                while right2>=0 and A[right2]==chr(32):
                    right2-=1
                A=A[:right2+1]
                #print A+"b"
                right=right2
                #A=A[:right+1]
            else:
                right-=1
        #print A,right
        temp.append(A[right+1:])
        
        return " ".join(temp)
