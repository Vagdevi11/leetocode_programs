class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        max_count=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
            else:
                max_count.append(count)
                
                count=1
        max_count.append(count)        
        return max(max_count)            
        