class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for user in accounts:
            userBal = 0
            for account in user:
                userBal = userBal + account
            maxWealth = max(maxWealth, userBal)
        
        return maxWealth


        