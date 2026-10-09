# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Reorder a linked list according to its midpoint."""
        slow_ptr = fast_ptr = head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        ptr = slow_ptr.next
        slow_ptr.next = None

        def reverse(head: ListNode) -> ListNode:
            curr = head
            prev = None

            while curr is not None:
                next_node = curr.next
                curr.next = prev 
                prev = curr
                curr = next_node

            return prev
        
        rev = reverse(ptr)

        while rev is not None:
            next_node = head.next
            head.next = rev
            rev = rev.next
            head.next.next = next_node
            head = head.next.next

