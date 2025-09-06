# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #Using HashSet for visited nodes
        """
        hashSet = set()
        curr = head

        while curr:
            if curr in hashSet :
                return True
            hashSet.add(curr)
            curr = curr.next

        return False
        """

        #using Floyd's Tortoise and Hare Cycle Detection 
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True # Cycle detected
        return False #No cycle present