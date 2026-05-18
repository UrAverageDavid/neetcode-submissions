class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # technically, you could just multiply all nums in the list then create a new list
        # with product / ith number
        # 0 is the problem: divide by 0 is not possible and total product will be 0
        # if contains 0:
        # save the index of 0, multiply the rest nonetheless
        # if more than one 0, array is just zeros
        # if one 0, the location of 0 is the product of all other nums and the rest are 0s
        zero_index = []
        answer = [0] * len(nums)
        product = 1
        for i, num in enumerate(nums):
            if num == 0: zero_index.append(i)
            else:
                product = product * num
        
        if len(zero_index) > 1:
            return answer
        elif len(zero_index) == 1:
            answer[zero_index[0]] = product
        else:
            for i, num in enumerate(nums):
                answer[i] = int(product / num)
        return answer
