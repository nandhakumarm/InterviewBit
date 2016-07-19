class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        myString=""
        
        while A>0:
            
            if A<=26:
                if A==0:
                    A=26
                myString=chr(A+64)+myString
                break
            if A>26:
                rem=A%26
                if rem==0:
                    rem=26
                    A-=26
                myString=chr(rem+64)+myString
            A=A/26
        return myString
