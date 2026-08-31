class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx=0
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if i!=j:
                    s=(nums[i]-1)*(nums[j]-1)
                    mx=max(s,mx)
        return mx            

        