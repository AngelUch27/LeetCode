#https://leetcode.com/problems/find-the-maximum-achievable-number/description/
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        for i in range(t):
            num +=2 

        return num
