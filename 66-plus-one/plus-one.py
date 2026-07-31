class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="".join(str(x) for x in digits)
        a=int(s)
        a=a+1
        ss=str(a)
        ans=[int(x) for x in ss]
        return ans
        