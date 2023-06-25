class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i for i in s.lower() if 'a' <= i <= 'z' or '0' <= i <= '9'])
        return True if s == s[::-1] else False
        