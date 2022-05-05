# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


def inorderTraversal(root) -> list[int]:
    if root == None:
        return []
    deq = deque([root])
    ans = []
    cur = deq[0]
    while cur.left:
        cur = cur.left
        deq.appendleft(cur)

    while deq:
        cur = deq.popleft()
        ans.append(cur.val)
        if cur.right:
            cur = cur.right
            deq.appendleft(cur)

            while cur.left:
                cur = cur.left
                deq.appendleft(cur)

    return ans
