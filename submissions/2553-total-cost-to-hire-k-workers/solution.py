class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left, right = [], []
        for _ in range(candidates):
            if not costs:
                break
            heappush(left, costs.pop(0))
            if not costs:
                break
            heappush(right, costs.pop())
        
        ret = 0
        for _ in range(k):
            if not left:
                ret += heappop(right)
                continue
            elif not right:
                ret += heappop(left)
                continue
            if left[0] < right[0]:
                ret += heappop(left)
                if costs:
                    heappush(left, costs.pop(0))
            elif left[0] == right[0]:
                if not costs:
                    ret += heappop(left)
                    continue
                if costs and costs[0] <= costs[-1]:
                    ret += heappop(left)
                    heappush(left, costs.pop(0))
                elif costs and costs[0] > costs[-1]:
                    ret += heappop(right)
                    heappush(right, costs.pop())
            else:
                ret += heappop(right)
                if costs:
                    heappush(right, costs.pop())

        return ret
            
                
