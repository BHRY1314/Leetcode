#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.67%)
# Total Accepted:    52.8K
# Total Submissions: 143.6K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
#
brackets="()"
Square_brackets="[]"
parantheses="{}"
# def str_to_dict(string):
#     dict_string={}
#     list_string=list(string)
#     for i in range(len(list_string)):
#         dict_string[list_string[i]]=i
#     return dict_string

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match={"(":")","{":"}","[":"]"}
        if(len(s)==0):
            return True
        if(len(s)%2!=0):
           return False
        else:
            for i in s:
                if(i in match):
                    stack.append(i)
                elif(stack==[] or match[stack.pop()]!=i):
                    return False
        return stack==[]




