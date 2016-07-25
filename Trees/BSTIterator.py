# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        
        self.myStack=[]
        temp=root
        while temp!=None:
            self.myStack.append(temp)
            temp=temp.left
        

    def hasNext(self):
        if len(self.myStack)!=0:
            return True
        

    def next(self):
        res=self.myStack.pop()
        temp=res
        if temp.right!=None:
            temp=temp.right
            #self.myStack.append(temp)
            #temp=temp.left
            while temp!=None:
                self.myStack.append(temp)
                temp=temp.left
        return res.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())