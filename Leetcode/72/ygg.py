class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        arr = [list(range(len(word2)+1))]
        j = 1
        for c in word1:
            arr.append([j] + [-1] * len(word2))
            j += 1

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    arr[i][j] = arr[i-1][j-1]
                else:
                    # min (insert, delete, replace)
                    arr[i][j] = min(arr[i-1][j] + 1, arr[i][j-1] + 1, arr[i-1][j-1] + 1)

        return arr[-1][-1]

    # def minDistance(self, word1: str, word2: str) -> int:
    #     arr = []
    #     cur = [0] * (len(word1) + 1)
    #
    #     for l2 in word2:
    #         prev = cur[:]
    #         arr.append(prev)
    #
    #         i = 1
    #         for l1 in word1:
    #             if l1 == l2:
    #                 cur[i] = prev[i-1] + 1
    #             else:
    #                 cur[i] = max(cur[i-1], prev[i])
    #             i += 1
    #
    #     arr.append(cur)
    #     print(arr)
    #
    #     l1 = len(word1)
    #     l2 = len(word2)
    #     ans = max(l1, l2)
    #     que = [[l2, l1, 0, 0]]
    #     while que:
    #         l2, l1, dis, remain = que.pop(0)
    #         queued = False
    #         print("p", l2, l1, dis, remain)
    #         while arr[l2][l1] > 0:
    #             print(l2, l1, dis, remain)
    #             if word1[l1 - 1] == word2[l2 - 1]:
    #                 # matched
    #                 dis += abs(remain)
    #                 remain = 0
    #                 l1 -= 1
    #                 l2 -= 1
    #             elif arr[l2][l1 - 1] == arr[l2 - 1][l1] and arr[l2][l1 - 1] > 0:
    #                 # push into queue
    #                 val = arr[l2][l1 - 1]
    #                 lt1 = l1
    #                 while arr[l2][lt1-1] == val:
    #                     lt1 -= 1
    #                 print("q", l2, lt1, dis, (l1 - lt1))
    #                 que.append([l2, lt1, dis, (l1 - lt1)])
    #                 lt2 = l2
    #                 while arr[lt2-1][l1] == val:
    #                     lt2 -= 1
    #                 print("q", lt2, l1, dis, -(l2 - lt2))
    #                 que.append([lt2, l1, dis, -(l2 - lt2)])
    #                 queued = True
    #                 break
    #
    #             elif arr[l2][l1 - 1] > arr[l2 - 1][l1]:
    #                 # remove from l1
    #                 if remain < 0:
    #                     dis += 1
    #                 remain += 1
    #                 l1 -= 1
    #             else:
    #                 # remove from l2
    #                 if remain > 0:
    #                     dis += 1
    #                 remain -= 1
    #                 l2 -= 1
    #
    #         if not queued:
    #             print("u", dis + max(l1, l2), dis, l2, l1)
    #             ans = min(ans, dis + max(l1, l2))
    #
    #     return ans


print(Solution.minDistance(Solution, "horse", "ros"))
print(Solution.minDistance(Solution, "intention", "execution"))
print(Solution.minDistance(Solution, "teacher", "aether"))
