# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        1. Find the middle of list
        2. Break and Reverse second half of list
        3. Merge the two lists
        """

        if not head or not head.next:
            return None
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None #break the lists

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #Merge the two lists
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
    