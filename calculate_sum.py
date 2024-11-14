from typing import List
import unittest


def calculate_sum(input_list : List[int]) -> int:
    return sum(input_list)


class TestCalculateSum(unittest.TestCase):
    def test_with_num_input(self):
        self.assertEqual(calculate_sum([1,2,3]), 6)
        self.assertEqual(calculate_sum([0,0,0]), 0)


if __name__ == "__main__":
    unittest.main()