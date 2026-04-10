# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfsPostOrder(node):
            nonlocal maxDiameter
            if not node:
                return 0
            
            leftHeight = dfsPostOrder(node.left)
            rightHeight = dfsPostOrder(node.right)

            curDiameter = leftHeight + rightHeight

            maxDiameter = max(maxDiameter, curDiameter)

            return 1 + max(leftHeight, rightHeight)

        dfsPostOrder(root)

        return maxDiameter