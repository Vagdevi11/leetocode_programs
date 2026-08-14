class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p=[0]
        s=0
        n=len(nums)
        for i in nums:
            s+=i
            p.append(s)
        for i in range(len(nums)):
            left_sum=p[i]
            right_sum=p[n]-p[i+1]
            if left_sum==right_sum:
                return i
        return -1        


        