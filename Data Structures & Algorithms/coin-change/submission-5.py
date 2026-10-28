class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hm = {0: 0}
        def dfs(amount):
            if amount in hm:
                return hm[amount]

            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            hm[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins