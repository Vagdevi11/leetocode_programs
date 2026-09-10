def canship(weights,days_have,capacity):
    #find the days_needed to ship all the weights under choosen capacity
    days_needed=1
    cWeightsum=0
    for w in weights:
        if cWeightsum+w<=capacity:
            cWeightsum+=w
        else:
            days_needed+=1
            cWeightsum=w
    return days_needed<=days_have            
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        capacity=max(weights)
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            if canship(weights,days,mid):
                high=mid
            else:
                low=mid+1
        return low            


        