class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = True
        for i in range(ord("a"), ord("z") + 1):
            if ransomNote.count(chr(i)) > magazine.count(chr(i)):
                result = False
                break
        return result