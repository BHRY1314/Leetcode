#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
class Solution:
    def climbStairs(self, n: int) -> int:
        con=[0]*n
        if n==1:
            return 1
        else:
            con[0]=1
            con[1]=2
            for i in range(2,n):
                con[i]=con[i-1]+con[i-2]
            return con[n-1]

