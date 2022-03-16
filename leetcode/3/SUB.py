class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_dic = {}
        ans = 0
        count = 0

        if s == "":
            return 0

        start_letter = s[0]

        for c in s:
            if c not in letter_dic:
                letter_dic[c] = count
            else:
                for el in list(letter_dic.keys()):
                    if letter_dic[el] < letter_dic[c]:
                        del letter_dic[el]
                letter_dic[c] = count

            count += 1
            ans = max(ans, len(letter_dic))

        return ans