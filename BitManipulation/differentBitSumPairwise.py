class Solution(object):
    def cntBits(self,A):
        total_difference=0
        for i in range(0,31):
            count_set=0
            count_not_set=0
            #temp=1<<i
            for j in A:
                j=j>>i
                if j&1==0:
                    count_not_set+=1
                else:
                    count_set+=1
            total_difference+=(2*count_not_set*count_set)
        return (total_difference)%((10**9)+7)
