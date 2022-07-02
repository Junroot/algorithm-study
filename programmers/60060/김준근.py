def compare(word, query):
    if len(word) < len(query):
        return -1
    elif len(word) > len(query):
        return 1

    for i in range(len(word)):
        if query[i] == '?':
            return 0
        if word[i] < query[i]:
            return -1
        if word[i] > query[i]:
            return 1
    return 0


def count_matches(words, query):
    start, end = 0, len(words)
    while start < end:
        mid = (start + end) // 2
        if compare(words[mid], query) < 0:
            start = mid + 1
        else:
            end = mid
    result1 = end

    start, end = 0, len(words)
    while start < end:
        mid = (start + end) // 2
        if compare(words[mid], query) <= 0:
            start = mid + 1
        else:
            end = mid
    result2 = end

    return result2 - result1


def solution(words, queries):
    words.sort(key=lambda x: (len(x), x))
    reversed_words = sorted(map(lambda x: x[::-1], words), key=lambda x: (len(x), x))
    result = []
    for query in queries:
        if query[0] == '?':
            result.append(count_matches(reversed_words, query[::-1]))
        else:
            result.append(count_matches(words, query))
    return result
