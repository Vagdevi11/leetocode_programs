class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count=0
        mx=max(nums)
        for i in range(len(nums)):
            count=count+mx-nums[i]
        return count        


        