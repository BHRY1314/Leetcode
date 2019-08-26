#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1:
            return s
        a=[[] for i in range(numRows)]
        r=0
        direct=1
        for c in s:
            a[r].append(c)
            if r>=numRows-1:
                direct=-1
            elif r==0:
                direct=1
            r+=direct
        answer=""
        for row in a:
            for col in row:
                answer=answer+col
        return answer
