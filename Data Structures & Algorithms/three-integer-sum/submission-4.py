class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list first from smallest -> largest
        # guarantees that primary index only traverses until 0
        # then, target = 0 - index num
        # two pointer search on the rest 
        # if target exists, add 3 nums to array & append to result array
        nums.sort()
        a, b = 0 ,0
        result = []
        for i, num in enumerate(nums):
            if num > 0: break
            if i > 0 and num == nums[i - 1]: continue
            target = 0 - num
            a  = i + 1
            b = len(nums) -1
            while a < b:
                if nums[a] + nums[b] > target:
                    b -= 1
                elif nums[a] + nums[b] < target:
                    a += 1
                else:
                    result.append([num, nums[a], nums[b]])
                    a += 1
                    b -= 1

                    while a < b and nums[a] == nums[a - 1]:
                        a += 1
                    while a < b and nums[b] == nums[b + 1]:
                        b -= 1
        return result

            

        