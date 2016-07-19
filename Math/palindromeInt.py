class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        myStr=str(A)
        left=0
        right=len(myStr)-1
        #print left,right,myStr
        while left<=right:
            if myStr[left]!=myStr[right]:
                return False
            left+=1
            right-=1
        return True
