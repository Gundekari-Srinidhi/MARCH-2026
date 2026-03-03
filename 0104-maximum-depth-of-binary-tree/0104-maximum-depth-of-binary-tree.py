# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        l=[]
        max1=0
        def preorder(node):
            nonlocal max1 
            if not node:
                return
            l.append(node.val)
            preorder(node.left)
            preorder(node.right)
            max1=max(max1,len(l))
            l.pop()
        preorder(root)
        return max1
        