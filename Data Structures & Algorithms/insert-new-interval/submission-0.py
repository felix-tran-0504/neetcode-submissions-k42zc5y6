class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        s_new, e_new = newInterval[0], newInterval[1]
        s_added, e_added = s_new, e_new
        for interval in intervals:
            s, e = interval[0], interval[1]
            if e < s_new:
                out.append(interval)
            elif s > e_new:
                out.append([s_added, e_added])
                out.extend(intervals[intervals.index(interval):])
                return out
            else:
                s_added = min(s, s_added)
                e_added = max(e, e_new)

        out.append([s_added, e_added])
        return out