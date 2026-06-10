class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lista: set = set()
        for i in nums:
            if i in lista:
                return True
            lista.add(i)
        return False
