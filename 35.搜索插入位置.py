#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index=0
        if target in nums:
            index=nums.index(target)
        else:
            for i,num in enumerate(nums):
                if(target>num):
                    index=i+1
                elif (target<num):
                    index=i
                    break
        return index

