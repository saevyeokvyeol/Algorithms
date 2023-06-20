from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_dic = Counter(ransomNote)
        mag_dic = Counter(magazine)

        for n in note_dic:
            if note_dic[n] > mag_dic[n]:
                return False
        return True
