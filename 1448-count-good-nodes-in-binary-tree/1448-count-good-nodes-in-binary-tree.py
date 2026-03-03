# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       
        l=[]
        count=0
        def preOrder(node,l):
            nonlocal count
            if not node:
                return
            l.append(node.val)
            if node.val==max(l):
                count+=1
            preOrder(node.left,l)
            preOrder(node.right,l)

            l.pop()
        preOrder(root,l)
        return count
        