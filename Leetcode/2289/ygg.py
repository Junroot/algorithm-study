def totalSteps(self, nums: list[int]) -> int:
    if len(nums) <= 1:
        return 0

    """
    # TLE
    popped = False
    step = 0
    while True:
        i = 1
        prev = nums[0]
        while i < len(nums):
            if nums[i] < prev:
                prev = nums.pop(i)
                popped = True
            else:
                prev = nums[i]
                i += 1
        # print(nums, popped)
        if popped:
            popped = False
            step += 1
        else:
            break

    return step
    """

    """
    # try 1. calc max step & linear
    max_step = 0

    i = 1
    prev = nums[0]
    while i < len(nums):
        if nums[i] < prev:
            step = 1
            prev = nums.pop(i)
            # try 1.2. [5,14,15,"2,11,5,13",15]
            # try 1.3. [1945, 1886, 346, 481, 1059, 1388, 1483, 1516, 1842, 1868, 1877, 398, 907, 995, 1167, 1214, 1423, 1452, 1464, 1474, 1311, 1427, 1757, 1992]
            prev_step = 1
            prev_max = prev
            while i < len(nums) and nums[i - 1] > nums[i]:
                if prev_max <= nums[i]:
                    step = max(prev_step, step) + 1
                    prev_max = nums[i]
                elif prev <= nums[i]:
                    step += 1
                # try 1.1. [10,1,2,3,4,5,6,"1,2,3"]
                else:
                    if step > prev_step:
                        prev_max = prev
                    elif step == prev_step:
                        prev_max = min(prev_max, prev)
                    print(nums, step, prev_step, prev_max)
                    max_step = max(step, max_step)
                    prev_step = max(step, prev_step)
                    step = 1
                prev = nums.pop(i)
            max_step = max(step, prev_step)
            # print(nums, step, max_step)
        else:
            prev = nums[i]
            i += 1

    return max_step
    """

    # try 2. multi stack
    ans = 0
    stacks = [[nums[0], 0]]

    for n in nums[1:]:
        m = 0
        while stacks and stacks[-1][0] <= n:
            v, s = stacks.pop()
            m = max(s, m)
        if stacks:
            m += 1
        else:
            m = 0
        stacks.append([n, m])
        ans = max(ans, m)

    return ans
