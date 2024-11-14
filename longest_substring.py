# Longest Substring Without Repeating Characters
# Input: "abcabcbb"
# Output: 3  # "abc"

import unittest

def get_substring_without_repeat(input_string: str) -> int:
    char_list = []
    max_length = 0
    for char in input_string:
        if char in char_list:
            char_list = char_list[char_list[char_list.index(char)] + 1:]
        char_list.append(char)
        # keeps the max length of the non-repeating substring when processing other non-repeating substrings
        # that might be shorter
        max_length = max(max_length, char_list.length())
    return char_list.length()

class TestGetSubStringWithoutRepeat(unittest.TestCase):
    def test_substring_1(self):
        self.assetEqual(get_substring_without_repeat("abcabcbb"), 3)
    def test_substring_2(self):
        self.assetEqual(get_substring_without_repeat("pwwkew"), 2)

if __name__ == "__main__":
    unittest.main()