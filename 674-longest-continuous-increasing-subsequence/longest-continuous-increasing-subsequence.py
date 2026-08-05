class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count=1
        max_count=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count+=1
            else:
                max_count=max(count,max_count)
                count=1

        return max(count,max_count)          

        