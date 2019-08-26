#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum=sum-root.val
        if sum==0:
            if root.left is None and root.right is None:
                return True
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)

