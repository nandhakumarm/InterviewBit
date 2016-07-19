class Solution(object):
    def pow(self, x, n,d):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        res_Pow=0
        #if n<0:
        #    isNeg=True
        #    n=-1*n
        #print x
        #print n
        if x==0:
            return 0
        if n==0:
            res_Pow=1
        elif n==1:
            res_Pow=x%d
        elif n%2==0:
            res_Pow= Solution.pow(self,(x**2)%d,n/2,d)
        elif n%2==1:
            res_Pow =(Solution.pow(self, (x**2)%d, (n-1)/2,d)*x)
        #if isNeg==True:
        #   return (1./res_Pow)%d
        return res_Pow%d
