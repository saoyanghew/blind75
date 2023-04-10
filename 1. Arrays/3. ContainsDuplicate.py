from typing import List

# brute-force, O(n2), O(1)

# sorting, O(nlogn), O(1)

# hash, O(n), O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False