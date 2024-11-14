# Reverse Words in a String
# Input: "The sky is blue"
# Output: "blue is sky The"
from typing import List
import unittest

def reverse_string(input_string: str) -> str:
    # split the sentence into list of words
    word_list = input_string.split()

    ## reverse the list
    word_list = word_list[::-1]

    # put the sentence back together
    return " ".join(word_list)

class TestReverseString(unittest.TestCase):
    def test_reverse_string_with_sentence(self):
        self.assertEqual(reverse_string("The sky is blue"), "blue is sky The")

if __name__ == "__main__":
    try:
        unittest.main()
    except Exception as e:
        raise e