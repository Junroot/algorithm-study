def solution(sales, links):
    sales = [0] + sales
    underlings = [[] for _ in range(len(sales))]
    for link in links:
        underlings[link[0]].append(link[1])

    cache = [-1 for _ in range(len(sales))]

    def get_min_cost(leader_index):
        if cache[leader_index] != -1:
            return cache[leader_index]
        if len(underlings[leader_index]) == 0:
            return 0
        children_sum = sum(get_min_cost(underling) for underling in underlings[leader_index])
        result = sales[leader_index] + children_sum

        for underling in underlings[leader_index]:
            temp = children_sum - get_min_cost(underling) + sales[underling]
            for temp_underling in underlings[underling]:
                temp += get_min_cost(temp_underling)
            result = min(temp, result)
        cache[leader_index] = result
        return result

    return get_min_cost(1)