def isValidBST(root) -> bool:
    if root == None:
        return True

    cur = root
    inord = []
    low = -(2**31) - 1
    high = 2**31

    while cur or inord:
        if cur:
            if not low < cur.val < high:
                return False
            inord.append([cur, low, high])
            high = cur.val
            cur = cur.left
        else:
            node, low, high = inord.pop()
            low = node.val
            cur = node.right

    return True