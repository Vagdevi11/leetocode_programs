class Solution:
    def largestEven(self, s: str) -> str:
        for i in range(len(s)):
            if int(s)%2==0:
                return s
            else:
                s=s[:len(s)-1]
        return ""        
