# stack
def largestRectangleArea(self, heights: List[int]) -> int:
    ans = 0
    st = []

    for i in range(len(heights)):
        while st and heights[st[-1]] > heights[i]:
            m = st.pop()
            if st:  # cor2: calc from prev height
                ans = max(ans, heights[m] * (i - st[-1] - 1))
            else:  # cor1: if first element, width = i
                ans = max(ans, heights[m] * i)
        st.append(i)

    # cor0: calc remainders
    prev = -1
    for i in st:
        ans = max(ans, heights[i] * (len(heights) - 1 - prev))
        prev = i

    return ans


# segment tree_not now
def calc(self, left, right, pos, tree, heights):
    if left == right:
        return heights[pos]
    mid = (left + right) / 2
    tree[pos] = calc(left, mid, pos * 2, tree, heights) + calc(mid, right, pos * 2 + 1, tree, heights)
    return tree[pos]

def largestRectangleArea(self, heights: list[int]) -> int:
    n = 1
    while n < len(heights):
        n *= 2
    tree = [0] * n  # * 2

    for h in heights:


    return
