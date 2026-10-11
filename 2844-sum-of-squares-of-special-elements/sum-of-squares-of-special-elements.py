class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        l=[]
        for i in range(1,len(nums)+1):
            if len(nums)%i==0:
                print(i)
                l.append(nums[i-1]**2)
        return sum(l)       