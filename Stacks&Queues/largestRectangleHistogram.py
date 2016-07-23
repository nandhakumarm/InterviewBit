class Solution(object):
    def largestRectangleArea(self,A):
        myStack=[]
        max_area=0
        i=0
        while i<len(A):
            if len(myStack)==0 or A[myStack[-1]]<=A[i]:
                myStack.append(i)
                i+=1
            else:
                top_index=myStack.pop()
                j=-1
                if len(myStack)==0:
                    j=i
                else:
                    j=i-myStack[-1]-1
                curr_area=A[top_index]*j
                #print curr_area
                if max_area<curr_area:
                    max_area=curr_area
        while len(myStack)!=0:
            top_index=myStack.pop()
            j=-1
            if len(myStack)==0:
                j=i
            else:
                j=i-myStack[-1]-1
            curr_area=A[top_index]*j
            #print curr_area,top_index,j
            if max_area<curr_area:
                max_area=curr_area
        return max_area

sol=Solution()
A=[2,1,5,6,2,3]
print sol.largestRectangleArea(A)

                