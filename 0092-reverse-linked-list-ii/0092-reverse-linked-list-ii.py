# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        prevLeft, curr = dummy, head

        #To reach till left indexed Node
        for i in range(left - 1):
            prevLeft = curr
            curr = curr.next

        #To reverse the nodes between left and right positions
        prev = None
        for i in range(right-left+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # To link the middle reversed list to remaining corner Nodes on both sides.
        prevLeft.next.next = curr
        prevLeft.next = prev

        return dummy.next
    


        
        