from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        return result
