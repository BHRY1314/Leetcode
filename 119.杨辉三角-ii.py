#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # if rowIndex==0:
        #     return [1]
        # if rowIndex==1:
        #     return [1,1]
        # nums=[]
        # nums.append([1])
        # nums.append([1,1])
        # for i in range(2,rowIndex+1):
        #     temp=[1]*(i+1)
        #     for j in range(1,len(temp)-1):
        #         temp[j]=nums[i-1][j-1]+nums[i-1][j]
        #     nums.append(temp)
        # return nums[rowIndex]

        ###优化
        p=[1]
        if not rowIndex:
            return p
        for i in range(rowIndex):
            p=[1]+[p[j]+p[j+1] for j in range(len(p)-1)]+[1]
        return p
