class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for i in operations:
            
            if i.lstrip('-').isdigit():
                l.append((int(i)))
            elif i=="C" and len(l)>0:
                l.remove(l[-1])
            elif i=="D" and len(l)>0:
                l.append(l[len(l)-1]*2)
            elif i=="+" and len(l)>1:
                l.append(l[-1]+l[-2])   
            print(l)     
        return sum(l)         



        