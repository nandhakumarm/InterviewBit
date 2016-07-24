class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self,A):
        myStack=[]
        myList=[]
        if A==None:
            return myStack
        myStack.append(A)
        while len(myStack)!=0:
            temp=myStack.pop()
            myList.append(temp.val)
            if temp.right!=None:
                myStack.append(temp.right)
            if temp.left!=None:
                myStack.append(temp.left)
        return myList

t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t4=TreeNode(4)
t1.left=t2
t1.right=t3
t3.left=t4
sol=Solution()
print sol.preorderTraversal(t1)