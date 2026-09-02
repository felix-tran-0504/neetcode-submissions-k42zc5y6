class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = {i: [] for i in range(numCourses)}
        for c1, c2 in prerequisites:
                hm[c1].append(c2)

        visit = set()

        def dfs(c):
            if c in visit:
                return False
            if hm[c] == []:
                return True
            visit.add(c)
            for p in hm[c]:
                if not dfs(p):
                    return False
            visit.remove(c)
            hm[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
