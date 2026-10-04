class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=[]
        x=s.split(" ")
        for word in x:
            if word.isdigit():
                l.append(int(word))     

        for i in range(len(l)-1):
            if l[i]>=l[i+1]:

                return False      
        return True        