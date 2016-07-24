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
        myStack=[]
        flag=1
        curr=A
        while flag:
            if curr!=None:
                myStack.append(curr)
                curr=curr.left
            else:
                if len(myStack)!=0:
                    curr=myStack.pop()
                    myList.append(curr.val)
                    curr=curr.right
                else:
                    flag=0
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