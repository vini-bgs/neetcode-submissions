class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = dict()
        for i, j in enumerate(nums):
            complemento = target - j
            if complemento in vistos:
                return [vistos[complemento],i]
            vistos[j] = i
