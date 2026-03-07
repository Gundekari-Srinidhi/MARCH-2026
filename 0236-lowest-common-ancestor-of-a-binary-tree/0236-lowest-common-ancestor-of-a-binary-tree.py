# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ls=[]
        def order(node,l,p,q):
            if not node:
                return
            ls.append(node)
            if node==p or node==q:
                l.append(ls.copy())
            order(node.left,l,p,q)
            order(node.right,l,p,q)
            ls.pop()            
            
        l=[]
        order(root,l,p,q)
        l[0]=l[0][::-1]
        l[1]=l[1][::-1]
        val1=max(len(l[0]),len(l[1]))
        for i in range(val1):
            if l[0][i] in l[1]:
                return l[0][i]

        