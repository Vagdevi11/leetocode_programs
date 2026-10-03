class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        x=""
        for i in range(0,k):
            x=x+s[i]
        x=x[::-1]
        ans=x+s[k:]
        return ans   
        