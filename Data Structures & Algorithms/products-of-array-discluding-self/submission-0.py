from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]
        res = [1] * (len(nums))

        # [1, 1, 2, 6]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # [24, 12, 8, 6]
        postfix = 1 
        for i in range(len(nums) - 1, -1 ,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res