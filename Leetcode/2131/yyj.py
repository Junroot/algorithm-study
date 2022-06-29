class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        N = len(words)
        words_counter = collections.Counter(words)
        two_same_letters_center = False
        res = 0
        
        for w in words_counter:
            if w[0] != w[1] and w[::-1] in words_counter:
                res += 2 * min(words_counter[w], words_counter[w[::-1]])
            elif w[0] == w[1]:
                pair_count = 2 * (words_counter[w] // 2)
                res += 2 * pair_count
                if words_counter[w] > pair_count:
                    two_same_letters_center = True
        
        return res if not two_same_letters_center else res + 2
