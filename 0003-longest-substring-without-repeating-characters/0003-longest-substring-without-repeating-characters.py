class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # If character already seen and is within the current window
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1  # move left pointer

            char_index[char] = right  # update last index of char
            max_length = max(max_length, right - left + 1)

        return max_length

        