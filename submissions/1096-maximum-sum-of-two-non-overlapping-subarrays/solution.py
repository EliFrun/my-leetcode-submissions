class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        firstLen, secondLen = max(firstLen, secondLen), min(firstLen, secondLen)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        best = 0
        
        q = [(-(prefix[i + secondLen] - prefix[i]), i) for i in range(firstLen, len(prefix) - secondLen)]
        heapify(q)

        for i in range(len(prefix) - firstLen):
            curr = prefix[i + firstLen] - prefix[i]
            if i >= secondLen:
                heappush(q, (- (prefix[i] - prefix[i - secondLen]), i - secondLen))
            
            # remove invalid intervals
            while q and i <= q[0][1] <= i + firstLen:
                heappop(q)
            if q:
                best = max(best, curr - q[0][0])

        return best


        
        
