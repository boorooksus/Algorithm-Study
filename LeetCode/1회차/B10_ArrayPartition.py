from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum


sol = Solution()
print(sol.arrayPairSum([1,4,2,3]))

# leetcode: 561