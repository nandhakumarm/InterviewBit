class Solution(object):
    def searchInsert(self, nums, target):
        
        index=0
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low + (high-low)/2
            if target<=nums[low]:
                return low
            elif target>nums[high]:
                return high+1
            elif target==nums[high]:
                return high
            elif nums[mid]==target:
                return mid
            elif target>nums[mid]:
                
                low=mid+1
            elif target<nums[mid]:
                high=mid-1
        return index
