class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self,A):
        myList=[]
        if A==None:
            return myList
        temp=A
        temp1=self.inorderTraversal(temp.left)
        for i in temp1:
            myList.append(i)
        myList.append(temp.val)
        temp2=self.inorderTraversal(temp.right)
        for i in temp2:
            myList.append(i)
        
        return myList

t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t4=TreeNode(4)
t1.left=t2
t1.right=t3
t3.left=t4
sol=Solution()
print sol.inorderTraversal(t1)