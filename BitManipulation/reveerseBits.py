class Solution(object):
    def reverse(self,A):
        for i in range(16):
            temp=32-1-i
            a=(A>>i)&1
            b=(A>>temp)&1
            if a^b!=0:
                A^=(1<<i)|(1<<temp)
        return A

