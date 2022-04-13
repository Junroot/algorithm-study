def minWindow(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""
    elif len(t) == 1:
        if s.find(t) >= 0:
            return t
        else:
            return ""

    l = len(t)
    T = {}
    for c in t:
        if c in T:
            T[c] += 1
        else:
            T[c] = 1

    a = 0
    pos = []
    ans = (-1, 100000)
    for i in range(len(s)):
        if s[i] in T:
            if T[s[i]] > 0:
                pos.append(i)
                T[s[i]] -= 1
                a += 1
            else:
                if s[i] == s[pos[0]]:
                    pos.pop(0)
                    while pos and T[s[pos[0]]] < 0:
                        T[s[pos[0]]] += 1
                        pos.pop(0)
                else:
                    T[s[i]] -= 1
                pos.append(i)
            if a == l:
                if ans[1] - ans[0] > pos[-1] - pos[0]:
                    ans = (pos[0], pos[-1])

    if ans[0] == -1:
        return ""
    else:
        return s[ans[0]:ans[1]+1]


print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a", "b"))
# 1글자 처리 t in s 로 불가능
print(minWindow("bba", "ab"))
# while T[s[pos[0]]] index out of range, pos 추가
print(minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))
# "bbcdd", 첫 else 문에서 T로 한 번 더 감쌌음 ( T[s[i]] )
print(minWindow("babb", "baba"))
# "b", 마지막 return 예외 처리 안 함
