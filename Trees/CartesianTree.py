class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        if len(A)==0:
            return None
        elif len(A)==1:
            root=TreeNode(A[0])
        else:
            temp=max(A)
            temp_index=A.index(temp)
            root=TreeNode(temp)
            root.left=self.buildTree(A[0:temp_index])
            root.right=self.buildTree(A[temp_index+1:])
        
        return root
        
