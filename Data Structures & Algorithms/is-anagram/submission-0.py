class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def g(s: str):
            hs = {}
            for i, val in enumerate(s):
                if val in hs:
                    hs[val] += 1
                else:
                    hs[val] = 1
            return hs
        
        h1 = g(s)
        h2 = g(t)

        for val in h1:
            if val not in h2:
                return False
            elif h1[val] != h2[val]:
                return False
        return True
