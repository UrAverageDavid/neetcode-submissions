class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # convert string to a mapping of letter frequency
        # use ord(char) to convert to ascii number, subract by a, get index
        def mapper(string: str) -> str:
            mapped_dict = [0] * 26
            for i, char in enumerate(string):
                index = ord(char) - ord("a")
                mapped_dict[index] += 1
            return "/".join(map(str, mapped_dict))
        s_mapped = mapper(s)
        t_mapped = mapper(t)
        return s_mapped == t_mapped