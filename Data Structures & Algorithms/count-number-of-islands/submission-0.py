class Solution:
    def DFS(self, coor: tuple(int, int)) -> list[tuple(int ,int)]:
        return [(coor[0], coor[1]+1), 
                (coor[0], coor[1]-1), 
                (coor[0]+1, coor[1]), 
                (coor[0]-1, coor[1])]
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    dfs = self.DFS((i, j))
                    while dfs:
                        curr = dfs.pop()
                        if curr[0] not in range(len(grid)) \
                        or curr[1] not in range(len(grid[0])):
                            continue
                        if grid[curr[0]][curr[1]] == "1":
                            grid[curr[0]][curr[1]] = "0"
                            dfs += self.DFS(curr)
                    count += 1
        return count
                        