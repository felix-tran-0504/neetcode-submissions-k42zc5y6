class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        out = []
        l = 0
        r = 0
        i = 0
        while i < len(intervals):
            l, r = intervals[i]

            j = i+1
            while j < len(intervals):
                x, y = intervals[j]
                if r >= x:
                    l = min(l, x)
                    r = max(r, y)
                    j += 1
                else:
                    break
            out.append([l, r])
            i = j

        return out