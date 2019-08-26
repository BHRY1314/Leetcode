#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # empty_list=[]
        # if s.find(" ")==-1:
        #     return len(s)
        # else:
        #     empty_list.append([i.start() for i in re.finditer(" ",s)])
        #     index=empty_list[0]
        #     if len(index)==1 and index[0]!=0:
        #         return index[0]
        #     elif len(index)==1 and index[0]==0:
        #         return len(s)-1
        #     else:
        #         num=0
        #         for i in range(len(index)-1):
        #             if index[i+1]-index[i]-1>0:
        #                 temp=index[i+1]-index[i]-1
        #                 if temp>num:
        #                     num=temp
        # if len(s)-index[-1]>num:
        #     num=len(s)-index[-1]-1
        # if index[0]-0>num:
        #     num=index[0]
        # return num
        l=len(s)
        if l==0:
            return 0
        n=l-1
        while n>=0:
            if s[n]==" ":
                n=n-1
            else:
                for i in range(n-1,-1,-1):
                    if s[i]==" ":
                        return n-i
                return n+1
        return 0
