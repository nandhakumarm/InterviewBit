class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    
    def getHeight(self,node):
        h=0
        if node==None:
            return 0
        return 1+max(self.getHeight(node.left),self.getHeight(node.right))
        
    def isBalanced(self, root):
        if root==None:
            return 1
        else:
            h=self.getHeight(root.left)-self.getHeight(root.right)
            if h<=1 and h>=-1 and self.isBalanced(root.left) and self.isBalanced(root.right):
                return 1
            else:
                return 0
            
t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t4=TreeNode(4)
t1.left=t2
t1.right=t3
t3.left=t4
sol=Solution()
print sol.isBalanced(t1)