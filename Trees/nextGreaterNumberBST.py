class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        curr=A
        while curr!=None:
            if B>curr.val:
                curr=curr.right
            elif B<curr.val:
                curr=curr.left
            elif B==curr.val:
                break
        
        if curr==None:
            return None
        if curr.right!=None:
            temp=curr.right
            while temp.left!=None:
                temp=temp.left
            return temp
        else:
            succ=None
            ancestor=A
            while curr!=ancestor:
                if curr.val<ancestor.val:
                    succ=ancestor
                    ancestor=ancestor.left
                else:
                    ancestor=ancestor.right
            return succ
        