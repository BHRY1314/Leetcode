#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=""
        list_num=[]
        for i in digits:
            num=num+str(i)
        num=int(num)+1
        list_num=[int(x) for x in str(num)]
        return list_num
