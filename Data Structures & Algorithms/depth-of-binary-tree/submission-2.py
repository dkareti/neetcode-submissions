# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Determine the maximum depth of a binary tree."""
        if not root:
            return 0
        
        level = 0
        queue = collections.deque([root])

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            level += 1 #iterates one value whenever the queue is not empty
        return level