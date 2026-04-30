class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        n = len(nums)
        for i in range(n-1):
            latest = pre[-1]
            pre.append(latest * nums[i])
        
        post = [1]
        for i in range(n-1, 0, -1):
            latest = post[-1]
            post.append(latest * nums[i])

        res = []
        for i in range(n):
            res.append(pre[i] * post[-(i+1)])
        
        
        return res