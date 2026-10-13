# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Perform an inorder traversal of the binary tree."""
        result = []
        stack = []
        ptr = root

        while ptr is not None or stack:
            while ptr is not None:
                stack.append(ptr)
                ptr = ptr.left
            ptr = stack.pop() 
            result.append(ptr.val)
            ptr = ptr.right
        
        return result