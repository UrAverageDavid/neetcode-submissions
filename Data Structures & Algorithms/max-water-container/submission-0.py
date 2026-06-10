class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = width (index1 - index2 - 1) * smallest height 
        # greedy move? (pointer with smaller index moves to keep updating the smallest index)
        def smallest(a, b):
            if a > b: return b
            else: return a
        i, j = 0, len(heights) - 1
        result = 0
        while i < j:
            area = (j - i) * smallest(heights[i], heights[j])
            if area > result: result = area
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return result
            