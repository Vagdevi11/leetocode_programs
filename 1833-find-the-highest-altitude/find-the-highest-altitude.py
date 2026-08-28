class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum=[]
        s=0
        for i in range(len(gain)):
            s+=gain[i]
            prefix_sum.append(s)
        return max(max(prefix_sum),0)    

        