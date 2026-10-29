class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = max(dp[i], dp[i] + dp[i+1])
        return max(dp)