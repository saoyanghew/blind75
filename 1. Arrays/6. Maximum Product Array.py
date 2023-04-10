from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)

        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * curMax, n * curMin, n)
            result = max(result, curMax)

        return result