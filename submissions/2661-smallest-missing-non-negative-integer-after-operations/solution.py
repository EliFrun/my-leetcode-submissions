class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        c = Counter([(x % value + value) % value for x in nums])
        m_count = float('inf')
        ret = float('inf')
        for i in range(value):
            if i not in c:
                m_count = 0
                ret = i
                break
            if c[i] < m_count:
                m_count = c[i]
                ret = i

        return value * m_count + ret
        
