#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices:
        #     return 0
        # i=0
        # j=1
        # max_profit=0
        # while j<=(len(prices)-1):
        #     if prices[i]>=prices[j]:
        #         i=j
        #         j+=1
        #     else:
        #         profit=prices[j]-prices[i]
        #         if profit>max_profit:
        #             max_profit=profit
        #         j+=1
        # return max_profit

        ###别人的解法
        if prices == []: return 0
        res = 0
        small =prices[0]
        for n in prices[1:]:
            small = min(n,small)
            if res < n - small:
                res = n - small
        return res


