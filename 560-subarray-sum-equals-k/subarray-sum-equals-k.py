class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #prefix+hashmap solution
        csum=0#this is our prefix sum
        sub_count=0 #how many subarrays have we seen with sum k
        seen={0:1}
        for i in nums:
            #compute prefix sum
            csum+=i
            #required prefix sum (prefix(l-1),history)
            req=csum-k
            #check if req in seen prefixes so far
            if req in seen:
                sub_count+=seen[req]
            #add the number of times we seen that prefix 
            #push the current prefix in hashmap
            seen[csum]=seen.get(csum,0)+1
        return sub_count    


        
        

        