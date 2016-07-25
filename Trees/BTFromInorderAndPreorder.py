class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.preIndex=0
    def buildTree(self, preorder, inorder):
        inLow=0
        inHigh=len(inorder)-1
        if inLow>inHigh:
            return None
        root=TreeNode(preorder[self.preIndex])
        self.preIndex+=1
        if inLow==inHigh:
            return root
        inorderIndexOfRoot=inorder.index(root.val)
        root.left=self.buildTree(preorder, inorder[0:inorderIndexOfRoot])
        root.right=self.buildTree(preorder, inorder[inorderIndexOfRoot+1:])
        
        return root
        