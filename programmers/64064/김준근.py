def is_matched(banned_username, username):
    if len(banned_username) != len(username):
        return False
    for i in range(len(banned_username)):
        if banned_username[i] != "*" and banned_username[i] != username[i]:
            return False
    return True


def solution(user_id, banned_id):
    matched_indexes = [[] for _ in range(len(banned_id))]

    for banned_index, banned_username in enumerate(banned_id):
        for user_index, username in enumerate(user_id):
            if is_matched(banned_username, username):
                matched_indexes[banned_index].append(user_index)

    result = set()

    def count_banned_ids_cases(banned_index, used_bitmap):
        if banned_index == len(banned_id):
            result.add(used_bitmap)
            return

        for matched_index in matched_indexes[banned_index]:
            if (used_bitmap >> matched_index) % 2 == 0:
                count_banned_ids_cases(banned_index + 1, used_bitmap | (1 << matched_index))

    count_banned_ids_cases(0, 0)

    return len(result)

