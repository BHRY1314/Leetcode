#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#
class Solution:
    def myAtoi(self, str: str) -> int:
        # str=str.strip()
        # if len(str)<=0:
        #     return 0
        # i=0
        # sign=1
        # num=0
        # if str[0]=='-':
        #     sign=-1
        #     i=i+1
        # if str[0]=='+':
        #     i=i+1

        # while i<len(str):
        #     if str[i]>='0' and str[i]<='9':
        #         num=10*num+int(str[i])
        #         i+=1
        #     else:
        #         break
        # if sign==-1:
        #     if num>2**31:
        #         return -2147483648
        #     else:
        #         return -num
        # if sign==1:
        #     if num>=2**31:
        #         return 2147483647
        #     else:
        #         return num

        ###别人的代码，利用正则表达式
        str = str.strip()
        try:
            #如果匹配不到，则没有整数，如果有，则直接转换
            res = re.search('(^[\+\-]?\d+)', str).group()
            res = int(res)
            res = res if res <= 2147483647 else 2147483647
            res = res if res >= -2147483648 else -2147483648
        except:
            res = 0
        return res


