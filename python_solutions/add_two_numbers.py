# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        node1 = l1
        node2 = l2
        length1=0
        length2=0
        while node1 is not None:
            length1+=1
            node1=node1.next
        while node2 is not None:
            length2+=1
            node2=node2.next
        node1=l1
        node2=l2
        if length1<length2:
            temp1 = node1
            temp2 = node2
            temp_list = l2
        else:
            temp1 = node2
            temp2 = node1
            temp_list = l1
        while temp1 is not None:
            if temp2.val + temp1.val >= 10:
                if temp2.next is not None:
                    temp2.next.val += (temp2.val + temp1.val)//10
                else:
                    temp2.next = ListNode((temp2.val + temp1.val)//10, None)
                temp2.val=(temp2.val + temp1.val)%10
            else:
                temp2.val+=temp1.val
            temp1=temp1.next
            temp2=temp2.next
        while temp2 is not None:
            if temp2.val >=10:
                temp2.val = temp2.val%10
                if temp2.next is not None:
                    temp2.next.val += 1
                else:
                    temp2.next = ListNode(1, None)
            temp2=temp2.next
        return temp_list