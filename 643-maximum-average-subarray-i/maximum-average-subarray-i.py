class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #brute force solution -fails due to len(n) can be as 
        #long as 10^5
        #generate all sub_arrays and keep the averages of those whose length is k
        """
        max_average=-100000000
        for start in range(len(nums)):
            for end in range(start,len(nums)):
                sub_sum=0
                for i in range(start,end+1):
                    sub_sum+=nums[i]
                if end-start==k-1:
                    avg=sub_sum/k
                    max_average=max(max_average,avg) 
        return max_average             """
        maxavg=-100000000
        left=0
        currentsum=0
        for right in range(len(nums)):
            currentsum+=nums[right]
            if right>=k-1:
                avg=currentsum/k
                maxavg=max(maxavg,avg)
                currentsum-=nums[left]
                left+=1
        return maxavg          
        