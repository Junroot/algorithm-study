case_count = int(input())

for _ in range(case_count):
    n = int(input())
    preferences = [None] + list(map(int, input().split()))
    parents = [None for _ in range(n + 1)]

    def find_parent(student):
        now = student
        while parents[now] is not None and parents[now] != now:
            now = parents[now]
        return now


    def cycle_size(student):
        count = 1
        now = preferences[student]
        while now != student:
            count += 1
            now = preferences[now]
        return count

    answer = n

    for student_index in range(1, len(preferences)):
        preference = preferences[student_index]
        parents[student_index] = find_parent(preference)
        if parents[student_index] == student_index:
            answer -= cycle_size(student_index)

    print(answer)

