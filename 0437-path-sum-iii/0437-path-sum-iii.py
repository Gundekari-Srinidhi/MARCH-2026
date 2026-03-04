# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        l=[]
        count=0
        def order(node):
            nonlocal count
            if not node:
                return 
            l.append(node.val)
            s=0
            for i in reversed(l):
                s+=i
                if s==targetSum:
                    count+=1
            order(node.left)
            order(node.right)
            l.pop()
    
        order(root)
        return count