class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        node = root
        while len(stack) > 0 or node:
            if node:
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
        return result
        
