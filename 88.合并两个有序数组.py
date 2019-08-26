#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if len(nums2)==0:
        #     pass
        # else:
        #     nums1[m:]=nums2
        #     temp=nums1[0]
        #     for i in range(len(nums1)):
        #         for j in range(len(nums1)-1):
        #             if nums1[j]>nums1[j+1]:
        #                 temp=nums1[j+1]
        #                 nums1[j+1]=nums1[j]
        #                 nums1[j]=temp
        index = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m -= 1
            else:
                nums1[index] = nums2[n]
                n -= 1
            index -= 1
        if m < 0:
            nums1[:n + 1] = nums2[:n + 1]



