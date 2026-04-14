class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        start = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            inter = intervals[i]
            if inter[0] < start:
                count += 1
                start = min(start, inter[1])
            else:
                start = inter[1]
        return count