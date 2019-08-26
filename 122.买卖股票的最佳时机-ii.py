#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices:
        #     return 0
        # i=0
        # j=1
        # max_profit=0
        # if len(prices)==2:
        #     if prices[j]>prices[i]:
        #         temp=prices[j]-prices[i]
        #         max_profit=max_profit+temp
        # while j<=((len(prices)-2)):
        #     if prices[i]>=prices[j]:
        #         i=j
        #         j+=1
        #     else:
        #         if prices[j+1]>=prices[j]:
        #             j+=1
        #         else:
        #             temp=prices[j]-prices[i]
        #             max_profit=max_profit+temp
        #             i=j
        #             j+=1
        #     if j==(len(prices)-1) and prices[j]>prices[i]:
        #                 temp=prices[j]-prices[i]
        #                 max_profit=max_profit+temp
        # return max_profit

        ###运用贪心算法
        ###第一天买入，如果第二天的价格大于买入价就卖，追求局部最优解
        if not prices:
            return 0
        max_profit=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                max_profit=max_profit+(prices[i+1]-prices[i])
        return max_profit

