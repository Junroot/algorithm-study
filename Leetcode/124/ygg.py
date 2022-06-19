# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # return max sum of closed path or open path from left or right
    def maxPath(self, root: Optional[TreeNode]):
        # [2, -1] root.val could be open path
        # [-6,null,3,2] add closed path to single child returns
        if root.left == None and root.right == None:
            return root.val, root.val
        elif root.left == None:
            rmax, rsum = self.maxPath(root.right)
            return max(root.val, rmax, rsum, root.val + rsum), max(root.val, root.val + rsum)
        elif root.right == None:
            lmax, lsum = self.maxPath(root.left)
            return max(root.val, lmax, lsum, root.val + lsum), max(root.val, root.val + lsum)

        lmax, lsum = self.maxPath(root.left)
        rmax, rsum = self.maxPath(root.right)
        return max(root.val, lmax, rmax, lsum, rsum, root.val + lsum + rsum), max(root.val, root.val + lsum,
                                                                                  root.val + rsum)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(self.maxPath(root))
