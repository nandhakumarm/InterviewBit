class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self,A):
        myList=[]
        stack1=[]
        stack2=[]
        if A==None:
            return stack2
        #temp=A
        stack1.append(A)
        while len(stack1)!=0:
            temp1=stack1.pop()
            stack2.append(temp1)
            if temp1.left!=None:
                stack1.append(temp1.left)
            if temp1.right!=None:
                stack1.append(temp1.right)
        
        stack2.reverse()
        for i in stack2:
            myList.append(i.val)
        return myList

t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t4=TreeNode(4)
t1.left=t2
t1.right=t3
t3.left=t4
sol=Solution()
print sol.postorderTraversal(t1)