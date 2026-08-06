class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=list(s)
        left=0
        count=0
        max_count=0
        for right in range(len(l)):
            if l[right] in "aeiou":
                count+=1
            if right>=k-1:
                max_count=max(count,max_count)
                if s[left] in "aeiou" :
                    count-=1
                left+=1
        return max_count        

        