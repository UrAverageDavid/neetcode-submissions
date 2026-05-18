class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I need to return the top k most frequent numbers, meaning I need to know how frequent the numbers are.
        # Hasmap of num -> freq seems decent, but top k most means it's best if the ordering is already sorted
        # from insertion
        # How to make it sorted? 
        # Bucket sort after hashmap

        # create a map of number to frequency
        freqList = {}
        for i, num in enumerate(nums):
            if num not in freqList:
                freqList[num] = 1
            else:
                freqList[num] += 1

        # sort the map by frequency
        sorted_result = {k: v for k,v in sorted(freqList.items(), key=lambda item: item[1], reverse=True)}

        answer = []
        for key, value in list(sorted_result.items())[:k]:
            answer.append(key)
        return answer

        

        