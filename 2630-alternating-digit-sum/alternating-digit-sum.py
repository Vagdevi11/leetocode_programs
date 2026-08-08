class Solution:
    def alternateDigitSum(self, n: int) -> int:
        l=list(str(n))
        s=0
        for i in range(len(l)):
            if i%2==0:
                s+=int(l[i])
            else:
                s-=int(l[i])
        return s            

        