class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s=0
        for i in range(len(accounts)):
            s=max(s,sum(accounts[i]))
        return s    