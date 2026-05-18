class Solution:
    # challenge: how do I differentiate between split indicator and actual string?
    # how to encode:
    # we need a separator (/, #, etc) to indicate separate words
    # say we encode the length of the letter at the beginning
    # [123true, @%@!sdv] => 7123true7@%@!sdv
    # from the next char from the indicator, count the number, expect another indicator
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i, word in enumerate(strs):
            length = len(word)
            encoded += str(length) + "#" + word
        return encoded

    # we need a read indicator
    # starting index for the first word would be 2, since 0 = length, 1 = # (start indicator)
    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            answer.append(word)
            i = j+1+length
        return answer

            

