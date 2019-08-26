#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def isTreeEnd(n):
            if n==None:
                return 1
            else:
                return 1+max(isTreeEnd(n.left),isTreeEnd(n.right))
        if root==None:
            return 0
        else:
            return max(isTreeEnd(root.left),isTreeEnd(root.right))

