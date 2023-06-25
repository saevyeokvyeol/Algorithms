class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s.lower() if char.isalnum()])
        print(s, s[::-1])
        return s == s[::-1]