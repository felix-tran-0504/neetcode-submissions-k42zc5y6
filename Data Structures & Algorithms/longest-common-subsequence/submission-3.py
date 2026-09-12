class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def l(i, j):
            if (i, j) in cache:
                return cache[(i,j)]
            elif i == len(text1) or j == len(text2):
                return 0
            elif text1[i] == text2[j]:
                cache[(i,j)] = 1 + l(i+1, j+1)
            else:
                cache[(i,j)] = max(l(i+1, j), l(i, j+1))
            return cache[(i, j)]
        return l(0,0)