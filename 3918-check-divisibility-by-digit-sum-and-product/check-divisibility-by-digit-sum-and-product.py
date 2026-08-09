class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        temp=n
        while n>0:
            digit=n%10
            s+=digit
            p=p*digit
            n=n//10
        x=s+p
        return temp%x==0

