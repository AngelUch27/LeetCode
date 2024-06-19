#https://leetcode.com/problems/score-of-a-string/description/
class Solution:
    def scoreOfString(self, s: str) -> int:
        numero = 0
        for char in range (len(s)-1):
            numero += abs(ord(s[char]) - ord(s[char+1]))
        return numero


        