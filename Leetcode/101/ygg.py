# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        cur = [root.left, root.right]
        exist = True

        while exist:
            exist = False
            l = len(cur)
            for i in range(l // 2):
                if cur[i] == None and cur[l - i - 1] == None:
                    continue
                elif cur[i] != None and cur[l - i - 1] != None and cur[i].val == cur[l - i - 1].val:
                    exist = True
                    continue
                else:
                    return False
            n = []
            for node in cur:
                if node != None:
                    n.append(node.left)
                    n.append(node.right)
                else:
                    n.append(None)
            del(cur)
            cur = n
        
        return True
                
        
