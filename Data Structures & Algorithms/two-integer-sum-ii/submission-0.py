class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing order: we only scan up to target - 1 (technically)
        # two pointer: left at min, right at max
        # required = target - min
        # decrement right until required is found/right's location smaller than required
        # increment min by 1 
        # repeat
        left = 0
        right = len(numbers) - 1
        while left < right:
            required = target - numbers[left]
            if numbers[right] > required:
                right -= 1
                continue
            elif numbers[right] == required:
                return [left + 1, right + 1]
            elif numbers[right] < required:
                left += 1
                continue
        

        