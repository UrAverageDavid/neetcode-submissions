class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a list of frequency map strings with the same index order as the original list
        # group those with the same frequency map into arr, append them.
        def frequency_map(word: str) -> str:
            freq_list = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                freq_list[index] += 1
            return "/".join(map(str, freq_list))   
        # map the frequency - list of words
        hashmap = {}
        for word in strs:
            freq = frequency_map(word)
            if freq not in hashmap:
                hashmap[freq] = []
            hashmap[freq].append(word)
        
        result = list(hashmap.values())
        return result