#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        cur=head
        pre=None
        while cur!=None:
            pre=cur
            cur=cur.next
            while cur!=None and cur.val==pre.val:
                pre.next=cur.next
                cur=cur.next
        return head



