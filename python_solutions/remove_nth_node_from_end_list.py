
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    #approach with length of list
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        copy = head
        length = 0
        while copy is not None:
            length += 1
            copy = copy.next
        if length == n:
            return head.next
        copy2 = head
        i = 1
        while i < length - n:
            i += 1
            copy2 = copy2.next
        if copy2.next is not None:
            copy2.next = copy2.next.next
        return head

    #second approach - n space between two pointers and move second pointer to the end
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        guard = ListNode(0)
        guard.next = head
        first = guard
        second = guard
        for _ in range(n):
            first = first.next
        while first.next is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return guard.next


