#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # if numRows==0:
        #     return None
        # if numRows==1:
        #     return [[1]]
        # if numRows==2:
        #     return [[1],[1,1]]
        # nums=[]
        # nums.append([1])
        # nums.append([1,1])
        # for i in range(2,numRows):
        #     temp=[1]*(i+1)
        #     for j in range(1,len(temp)-1):
        #         temp[j]=nums[i-1][j-1]+nums[i-1][j]
        #     nums.append(temp)
        # return nums
        
        ##大神的代码
        r = [[1]]
        for i in range(1,numRows):
            r.append(list(map(lambda x,y:x+y, [0]+r[-1],r[-1]+[0])))
        return r[:numRows]#这里太强了


