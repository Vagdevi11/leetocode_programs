class Solution:
    def secondHighest(self, s: str) -> int:
        l=[]
        for ch in s:
            if ch.isdigit() and int(ch) not in l:
                l.append(int(ch))
        l.sort()
        if len(l)>=2:
            return l[-2]
        return -1      

