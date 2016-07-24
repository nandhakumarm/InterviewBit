class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        stack1=[]
        stack2=[]
        if root==None:
            return True
        if root.left==None and root.right==None:
            return True
        if (root.left==None and root.right!=None) or (root.left!=None and root.right==None):
            return False 
        stack1.append(root.left)
        stack2.append(root.right)
        while len(stack1)!=0 and len(stack2)!=0:
            temp1=stack1.pop()
            temp2=stack2.pop()
            if temp1.val!=temp2.val:
                return False
            if temp1.right!=None and temp2.left!=None:
                stack1.append(temp1.right)
                stack2.append(temp2.left)
            elif temp1.right==None and temp2.left==None:
                pass
            else:
                return False
            if temp1.left!=None and temp2.right!=None:
                stack1.append(temp1.left)
                stack2.append(temp2.right)
            elif temp1.left==None and temp2.right==None:
                pass
            else:
                return False
        
        if len(stack1)!=0 or len(stack2)!=0:
            return False
        return True