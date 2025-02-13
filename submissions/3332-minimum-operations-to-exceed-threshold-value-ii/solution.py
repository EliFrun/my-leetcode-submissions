class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        h = [num for num in nums if num < k]
        heapify(h)

        count = 0
        while h:
            count += 1
            if len(h) == 1:
                break
            num1, num2 = heappop(h), heappop(h)
            if 2 * num1 + num2 < k:
                heappush(h, 2 * num1 + num2)
        return count
