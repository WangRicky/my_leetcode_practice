# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        count = 1
        sums = l1.val
        while l1.next:
            sums = sums + l1.next.val * (10 ** count)
            l1 = l1.next
            count = count + 1
        count = 1
        sums = sums + l2.val
        while l2.next:
            sums = sums + l2.next.val * (10 ** count)
            l2 = l2.next
            count = count + 1
        sums = str(sums)[::-1]
        listnode = ListNode(sums[0])
        curNode = listnode
        for z in sums[1:]:
            temp = ListNode(z)
            curNode.next = temp
            curNode = temp
        return listnode