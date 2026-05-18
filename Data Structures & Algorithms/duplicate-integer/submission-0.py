class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = {}
        for i, num in enumerate(nums):
            if num not in exists:
                exists[num] = 1
            if exists[num] > 1:
                return True
            else:
                exists[num] = exists[num] + 1
        return False