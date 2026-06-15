import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        temp=head
        n=0
        while temp:
            temp=temp.next
            n+=1
        mid=math.ceil((n+1)/2)
        temp=head
        prev=temp
        for i in range(mid-1):
            prev=temp
            temp=temp.next
        prev.next=temp.next
        return head