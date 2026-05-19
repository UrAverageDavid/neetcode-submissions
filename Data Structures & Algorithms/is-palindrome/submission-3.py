class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ignore non-alphanumeric str.isalnum() 
        # compare using str.lower() to ensure accurate comparison
        i = 0
        j = len(s) - 1
        while i < j:
            # first skip if index is non-alphanumeric
            if not s[i].isalnum() or s[i] == " ": 
                i += 1
                continue
            if not s[j].isalnum() or s[j] == " ": 
                j -= 1
                continue
            # compare 
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
                continue
            else:
                return False
        return True
        
        