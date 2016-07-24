class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self,A,B):
        if A==None and B==None:
            return True
        temp1=A
        temp2=B
        if (temp1==None and temp2!=None) or (temp1!=None and temp2==None):
            return False
        elif temp1.val!=temp2.val:
            return False
        elif self.isSameTree(temp1.left, temp2.left) and self.isSameTree(temp1.right, temp2.right):
            return True
        else:
            return False 