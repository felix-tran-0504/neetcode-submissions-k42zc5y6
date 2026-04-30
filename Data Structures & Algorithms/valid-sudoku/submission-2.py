class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hm_i = {}
        hm_j = {}
        hm_square = {}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                if i not in hm_i:
                    hm_i[i] = []
                if val in hm_i[i]:
                    return False
                hm_i[i].append(val)

                if j not in hm_j:
                    hm_j[j] = []
                if val in hm_j[j]:
                    return False
                hm_j[j].append(val)

                i_square = i // 3
                j_square = j // 3
                square = (i_square, j_square)
                
                if square not in hm_square:
                    hm_square[square] = []
                if val in hm_square[square]:
                    return False
                hm_square[square].append(val)
        return True