class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        x=[]
        for i in range(len(nums)):
            mx=max(nums[0:i+1])
            mn=min(nums[i:len(nums)])
            if mx-mn<=k:
                x.append(i)
        if x!=[]:
            return min(x)
        return -1            
                

