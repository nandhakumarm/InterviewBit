class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None
        elif len(nums)==1:
            root=TreeNode(nums[0])
        low=0
        high=len(nums)-1
        if low<high:
            mid=low+((high-low)/2)
            root=TreeNode(nums[mid])
            root.left=self.sortedArrayToBST(nums[0:mid])
            root.right=self.sortedArrayToBST(nums[mid+1:])
        else:
            root=TreeNode(nums[0])
        return root
        
    