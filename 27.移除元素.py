#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=len(nums)
        if(l==0):
            return 0
        else:
            i=0
            while i < len(nums):
                print(i)
                if(nums[i]==val):
                    nums.pop(i)
                    if(i==0):
                        i=0
                    else:
                        i=i-1
                else:
                    i=i+1


