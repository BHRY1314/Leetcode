#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
class Solution:
    def mySqrt(self, x: int) -> int:
        g=x
        while (abs(g*g-x)>0.000001):
            g=(g+x/g)/2
        return int(g)

