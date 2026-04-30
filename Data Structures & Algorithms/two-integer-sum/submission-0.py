class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            k = target - n
            if n in hm:
                return [hm[n], i]
            hm[k] = i
        return hm