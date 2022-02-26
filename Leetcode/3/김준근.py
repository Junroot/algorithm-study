class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        longest_substring = ""
        length = 0
        for character in s:
            index = longest_substring.find(character)
            longest_substring = longest_substring[index + 1:] + character
            length = length - index
            result = max(result, length)
        return result
