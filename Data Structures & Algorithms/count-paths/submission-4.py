class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        
        def dfs(a: int, b: int) -> int:
            if a == m-1 and b == n-1:
                return 1
            if a >= m or b >= n:
                return 0
            if memo[a][b] != -1:
                return memo[a][b]
            
            memo[a][b] = dfs(a+1, b) + dfs(a, b+1)
            return memo[a][b]

        return dfs(0, 0)