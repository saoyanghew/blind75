from typing import List

class Solution:
    def maxAreaBruteForce(self, nums: List[int]) -> int:
        res = 0

        for l in range(len(nums)):
            for r in range(l + 1, len(nums)):
                area = (r - l) * min(nums[l], nums[r])
                res = max(res, area)
        
        return res
    
    def maxAreaActual(self, nums: List[int]) -> int:
        res = 0

        l, r = 0, len(nums) - 1

        while l < r:
            area = (r - l) * min(nums[l], nums[r])
            res = max(area, res)

            if nums[l] < nums[r]:
                l += 1
            
            elif nums[l] >= nums[r]:
                r -= 1

        return res