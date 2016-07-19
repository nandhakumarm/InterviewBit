class Solution(object):
    def maxset(self,A):
        max_sum = 0;
        cur_sum = 0;
        startmax = -1;
        endmax = -1;
        start = 0;
        end = 0;
        while end < len(A):
            if A[end]>=0:
                cur_sum += A[end]
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    startmax = start
                    endmax = end + 1
                elif(cur_sum == max_sum):
                    
                    if end + 1 - start > endmax - startmax:
                        startmax = start
                        endmax = end + 1
            else:
                start=end + 1
                cur_sum=0
            end+=1
        ans=[]
        if startmax == -1 or endmax == -1:
            return ans
 
        for i in range(startmax,endmax):
            ans.append(A[i])
        return ans

