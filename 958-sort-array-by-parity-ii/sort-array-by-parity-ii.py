class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
    
        even=[]
        odd=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        ans=[]
        x=0
        y=0
        for i in range(len(nums)):
            if i%2==0:
                ans.append(even[x])
                x+=1
            else:
                ans.append(odd[y])    
                y+=1
        return ans     
        
        


        