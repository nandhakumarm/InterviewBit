class Solution(object):
    def getMinIndex(self,nums):
        low=0
        high=len(nums)-1
        length=len(nums)
       
        #print "her"
        while low<=high:
            #print "klj"
            if nums[low]<=nums[high]:
                return low
            #mid=low+(high-low)/2
            mid=(high+low)/2
            nextt=(mid+1)%length
            prev=(mid-1+length)%length
            #print nums[prev],nums[nextt]
            if nums[mid]<=nums[prev] and nums[mid]<=nums[nextt]:
                return mid
            elif nums[low]<=nums[mid]:
                low=mid+1
            elif nums[high]>=nums[mid]:
                high=mid-1
            #print mid,high,low
        return -1
    def search(self, nums, target):
        
        low=0
        min_index=Solution.getMinIndex(self, nums)
        length=len(nums)
        high=length-1
        #print min_index
        if min_index==0:
            low=min_index
        elif target>=nums[min_index] and target<=nums[high]:
            low=min_index
        elif target<=nums[min_index-1] and target>=nums[low]:
            high=min_index-1
        while low<=high:
            mid=low+(high-low)/2
            #print mid,low,high
            if nums[mid]==target:
                return mid
            elif target<=nums[mid]:
                high=mid-1
            elif nums[mid]<=target:
                low=mid+1
        return -1
