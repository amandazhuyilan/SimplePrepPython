# Find the Intersection of Two Arrays
# Problem: Given two arrays, write a function to compute their intersection (elements common to both arrays).
# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]

from typing import List
import unittest

def find_intersection(input_array_1: List[int], input_array_2: List[int]) -> List[int]:
    """
    Find the intersection of two int lists.

    Args:
        input_array_1 (List[int]): input array 1
        input_array_2 (List[int]): input array 2
    
    Return:
        List[int]: the intersected list
    """
    intersection_set = set()

    for num_1 in input_array_1:
        for num_2 in input_array_2:
            if num_1 == num_2:
                intersection_set.add(num_1)  
    return list(intersection_set)

class TestFindIntersection(unittest.TestCase):
    def test_array_1(self):
        self.assertEqual(find_intersection([1,2,2,1], [2, 2]), [2])

if __name__ == "__main__":
    unittest.main()