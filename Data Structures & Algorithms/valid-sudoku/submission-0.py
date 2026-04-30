class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hm_i = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
        hm_j = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
        hm_square = {(0,0): [], (0,1): [], (0,2): [], 
                    (1,0): [], (1,1): [], (1,2): [], 
                    (2,0): [], (2,1): [], (2,2): []}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in hm_i[i]:
                    return False
                hm_i[i].append(val)
                if val in hm_j[j]:
                    return False
                hm_j[j].append(val)

                i_square = i // 3
                j_square = j // 3
                square = (i_square, j_square)
                
                if val in hm_square[square]:
                    return False
                hm_square[square].append(val)
        return True