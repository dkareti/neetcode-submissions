# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge two sorted linked lists."""
        dummy = ListNode()
        ptr = dummy

        while list1 is not None or list2 is not None:
            val1 = list1.val if list1 is not None else float('inf')
            val2 = list2.val if list2 is not None else float('inf')

            if val1 < val2:
                digit = val1
                list1 = list1.next if list1 is not None else None
            else: 
                digit = val2
                list2 = list2.next if list2 is not None else None

            node = ListNode(digit)
            ptr.next = node
            ptr = ptr.next

          
        return dummy.next