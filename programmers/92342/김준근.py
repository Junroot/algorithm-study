def solution(n, info):
    apeach_score = 0
    scores = []

    for i, count in enumerate(info):
        score = 10 - i
        if count == 0:
            scores.append(score)
            continue
        scores.append(score * 2)
        apeach_score += score

    def get_max_score(cache_index, left_arrow, used_arrows):
        if cache_index == 10:
            return [0, used_arrows + [left_arrow]]
        result = get_max_score(cache_index + 1, left_arrow, used_arrows + [0])
        if left_arrow >= info[cache_index] + 1:
            result2 = get_max_score(cache_index + 1, left_arrow - info[cache_index] - 1, used_arrows + [info[cache_index] + 1])
            result2[0] += scores[cache_index]
            if result2[0] > result[0]:
                return result2
            if result2[0] == result[0]:
                for i in range(10, -1, -1):
                    if result2[1][i] > result[1][i]:
                        return result2
                    elif result2[1][i] < result[1][i]:
                        return result
        return result

    lion_score = get_max_score(0, n, [])
    if lion_score[0] <= apeach_score:
        return [-1]
    return lion_score[1]
