class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self,A):
        length=len(A)
        carry=0
        temp=int(A[length-1])+1
        if temp<10:
            A[length-1]=temp
        elif temp>=10:
            carry=1
            A[length-1]=0
        i=length-2
        while carry!=0 and i>=0:
            temp=A[i]+carry
            if temp<10:
                A[i]=temp
                carry=0
            elif temp>=10:
                A[i]=0
                carry=1
            i-=1
        if carry==1:
            return [1]+A
        else:
            index=0
            for i in range(len(A)):
                if A[i]!=0:
                    index=i
                    break
            return A[index:]

