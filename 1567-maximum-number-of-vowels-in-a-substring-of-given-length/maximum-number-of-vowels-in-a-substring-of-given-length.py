def is_v(ch):
    return ch in "aeiou"
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
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
        """
        first_window=s[:k]
        v_c=0
        for i in first_window:
            if is_v(i):
                v_c+=1
        mx_v=max(v_c,0)
        #sliding window logic
        for i in range(k,len(s)):
            if is_v(s[i]):
                v_c+=1
            if is_v(s[i-k]):
                v_c-=1
            mx_v=max(mx_v,v_c)
        return mx_v                   


        