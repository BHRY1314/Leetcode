#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=0
        d={}
        start=0
        for i in range(len(s)):
            if s[i] in d and start<=d[s[i]]:
                start=d[s[i]]+1
            temp=max(i-start+1,temp)
            d[s[i]]=i
        return temp
