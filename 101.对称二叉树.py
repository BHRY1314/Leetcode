#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSameTree(r,l):
            if not r and not l:
                return True
            if r and l and r.val==l.val:
                q=isSameTree(r.right,l.left)
                p=isSameTree(l.right,r.left)
                return q and p
            else:
                return False
        if not root:
            return True
        else:
            return isSameTree(root.right,root.left)


