# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        ans = []
        cur = [root]
        
        while cur:
            a = []
            for node in cur:
                a.append(node.val)
            ans.append(a)
            
            n = []
            for node in cur:
                if node.left:
                    n.append(node.left)
                if node.right:
                    n.append(node.right)
            cur = n
            
        return ans
