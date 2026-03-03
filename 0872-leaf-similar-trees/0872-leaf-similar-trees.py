# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def order(node,l):
            if not node:
                return
            if not node.left and not node.right:
                l.append(node.val)
                return
            order(node.left,l)
            order(node.right,l)
            return l
        l1=[]
        val1=order(root1,l1)
        l2=[]
        val2=order(root2,l2)
        return l1==l2

        