#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        b=int(b,2)
        return bin(a+b)[2:]

