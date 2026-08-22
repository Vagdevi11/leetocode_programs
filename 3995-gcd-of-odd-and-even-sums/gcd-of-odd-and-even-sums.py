class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        evensum=0
        oddsum=0
        for i in range(1,(2*n)+1):
            if i%2==0:
                evensum+=i
            else:
                oddsum+=i
        x=math.gcd(oddsum,evensum)
        return x            
        