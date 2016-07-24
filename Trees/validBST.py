class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSubtreeLesser(self,root,value):
        if root==None:
            return 1
        if root.val<=value and self.isSubtreeLesser(root.left, value)==1 \
            and self.isSubtreeLesser(root.right, value)==1:
            return 1
        else:
            return 0
    def isSubtreeGreater(self,root,value):
        if root==None:
            return 1
        if root.val>value and self.isSubtreeGreater(root.left, value)==1 \
            and self.isSubtreeGreater(root.right, value)==1:
            return 1
        else:
            return 0
    def isValidBST(self, A):
        if A==None:
            return 1
        if self.isSubtreeLesser(A.left, A.val)==1 and \
            self.isSubtreeGreater(A.right, A.val)==1 and \
            self.isValidBST(A.left)==1 and self.isValidBST(A.right)==1:
            return 1
        else:
            return 0
        
            
#7 4 -1 5 3 -1 -1 -1
t1=TreeNode(4)
t2=TreeNode(5)
t3=TreeNode(3)
#t4=TreeNode(3)
#t1.left=t2
t1.right=t2
t2.left=t3
sol=Solution()



print sol.isValidBST(t1)