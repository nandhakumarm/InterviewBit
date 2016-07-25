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
    def kthsmallest(self, root, k):
        myList=self.inorderTraversal(root)
        return myList[k-1]