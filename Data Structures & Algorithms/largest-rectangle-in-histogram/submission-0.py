class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        n = len(heights)

        for i in range(n+1):
            while stack and (i == n or heights[i] < heights[stack[-1]]):
                h = heights[stack.pop()]
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                maxArea = max(maxArea, h * w)
            stack.append(i)
        return maxArea