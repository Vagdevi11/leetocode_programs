class Solution:
    def countRotations(self, s: str, k: int) -> int:
        count=0
        score=0
        for i in range(len(s)):
            s=s[1:]+s[0]
            for ch in range(len(s)-1):
                if s[ch]==s[ch+1]:
                    score+=1
            if score==k:
                count+=1
            score=0
        return count    
                    
        
        