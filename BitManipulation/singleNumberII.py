class Solution(object):
    def singleNumber(self, A):
        isNeg=False
        count_neg=0
        for i in A:
            if i<0:
                count_neg+=1
        if count_neg%3!=0:
            isNeg=True
        result=0
        for i in range(0,31):
            count=0
            temp=1<<i
            for j in A:
                if j&temp:
                    count+=1
            #count%=3
            #print count
            if count%3!=0:
                result|=temp
        temp=1<<31
        
        
        if isNeg==True:
            return result-2147483648
        else:
            return result

