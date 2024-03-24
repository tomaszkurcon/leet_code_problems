# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        if p1 is None: return p2
        if p2 is None: return p1
        if p1.val < p2.val:
            h = p1
            p1 = p1.next
        else:
            h = p2
            p2 = p2.next
        r = h
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                r.next = p1
                r = r.next
                p1 = p1.next
            else:
                r.next = p2
                r = r.next
                p2 = p2.next
        while p1 is not None:
            r.next = p1
            p1 = p1.next
            r = r.next
        while p2 is not None:
            r.next = p2
            p2 = p2.next
            r = r.next
        return h

