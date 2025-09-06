# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        #using Hashset of Visited nodes O(n)
        hashSet = set()
        curr = head

        while curr:
            if curr in hashSet:
                return curr
            hashSet.add(curr)
            curr = curr.next

        return None
        """
        #using Floyd's Tortoise and Hare Cycle detection
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast # Return fast or slow, they are at the same node
        