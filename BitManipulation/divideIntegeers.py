class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        isNegative=False
        if dividend<0 and divisor>0:
            isNegative=True
            dividend=-1*dividend
        elif dividend>=0 and divisor<0:
            isNegative=True
            divisor=-1*divisor
        elif dividend<0 and divisor<0:
            dividend=-1*dividend
            divisor=-1*divisor
        if dividend==0:
            return 0
        if dividend<divisor:
            return 0
        quo=0
        count=1
        while divisor<=dividend:
            #print "1"
            divisor=divisor<<1
            count=count<<1
        #print divisor,dividend,count
        while count>1:
            divisor=divisor>>1
            count>>=1
            if dividend>=divisor:
                dividend-=divisor
                quo+=count
        if isNegative:
            quo= -1*quo
        if quo>2147483647:
            return 2147483647
        elif quo<-2147483648:
            return -2147483648
        return quo

