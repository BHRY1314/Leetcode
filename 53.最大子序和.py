#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_num=nums[0]
        temp=0
        for i in range(len(nums)):
            if temp>0:
                temp=nums[i]+temp
            else:
                temp=nums[i]
            if sum_num<temp:
                sum_num=temp
        return sum_num
