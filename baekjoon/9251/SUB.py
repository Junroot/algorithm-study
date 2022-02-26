word1 = input()
word2 = input()

LCS = [[0] * (len(word2) + 1) for _ in range((len(word1)) + 1)]
ans = -1

for i in range(1, len(word1) + 1):
    for j in range(1, len(word2) + 1):
        if word1[i - 1] == word2[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
            if LCS[i][j] > ans:
                ans = LCS[i][j]
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
            if LCS[i][j] > ans:
                ans = LCS[i][j]

print(ans)
