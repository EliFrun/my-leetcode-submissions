class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            return list(str(int(''.join([str(s) for s in digits])) + 1))
