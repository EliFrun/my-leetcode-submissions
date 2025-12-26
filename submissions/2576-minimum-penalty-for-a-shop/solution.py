class Solution:
    def bestClosingTime(self, customers: str) -> int:

        left = 0
        right = customers.count('Y')
        ret = -1
        mi = float('inf')

        for i,c in enumerate(customers + '.'):
            if left + right < mi:
                mi = left + right
                ret = i
            if c == 'N':
                left += 1
            else:
                right -= 1

        return ret
