class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count=0
        mx=max(nums)
        for i in range(len(nums)):
            while nums[i]!=mx:
                nums[i]+=1
                count+=1
        return count        


        