class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        length=len(A)
        rankk=1
        import math
        fact=math.factorial(length)
        count=[0]*256
        
        for i in A:
            #if i>='a' and i<='z':
            count[ord(i)]+=1
        #print count
        for i in range(1,256):
            count[i]+=count[i-1]
        #print count
        for i in range(0,length):
            fact/= (length-i)
            #print rankk
            rankk+=(count[ord(A[i])-1] * fact)
            #print rankk,count[ord(A[i])-1],fact
            for i in range(ord(A[i]),256):
                count[i]-=1
            #print count
        return rankk%1000003
