class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_cap = 0
        while l < r:
            cap = min(heights[l], heights[r]) * (r-l)
            max_cap = max(max_cap, cap)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_cap