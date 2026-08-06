class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        left=0
        sm=0
        count=0
        for right in range(len(arr)):
            sm+=arr[right]
            if right>=k-1:
                avg=sm/k
                if avg>=threshold:
                    count+=1
                sm-=arr[left]
                left+=1
        return count 
        """
        #another approach of sliding window concept
        first_window=arr[:k]
        count=0
        current_sm=sum(first_window)
        if current_sm/k>=threshold:
            count+=1    
        for i in range(k,len(arr)):
            current_sm=current_sm+arr[i]-arr[i-k]
            if current_sm/k>=threshold:
                count+=1
        return count               




        