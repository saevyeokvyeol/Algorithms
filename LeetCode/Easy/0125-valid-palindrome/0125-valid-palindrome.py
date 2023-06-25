class Solution:
    # 내 풀이
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i for i in s.lower() if 'a' <= i <= 'z' or '0' <= i <= '9'])
        print(s, s[::-1])
        return True if s == s[::-1] else False

    # 리스트로 변환해 풀기
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # isalnum(): 영문자, 숫자 판별 함수
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True