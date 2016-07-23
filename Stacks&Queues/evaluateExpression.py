class Solution(object):
    def evaluate(self,a,b,op):
        if op=='+':
            return a+b
        elif op=='-':
            return a-b
        elif op=='*':
            return a*b
        elif op=='/':
            return a/b
    
    def evalRPN(self,A):
        if len(A)==1:
            return int(A[0])
        opStack=[]
        valStack=[]
        for i in A:
            if i!='+' and i!='-' and i!='*' and i!='/':
                valStack.append(i)
            else:
                b=int(valStack.pop())
                a=int(valStack.pop())
                valStack.append(Solution.evaluate(self, a, b,i))
        if len(valStack)!=1:
            return 0
        return valStack.pop()

sol=Solution()
A=["2", "2", "+", "3","*"]
B=[ "-500", "-10", "/"]
C=["-9"]
print sol.evalRPN(B)