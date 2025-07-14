class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        def solve(left, lis):
            if left == 1:
                return [lis[1] if lis[1] != 0 else lis[0]]
            diff = lis[-1] - lis[-2]
            l1, l2 = SortedList(), SortedList()
            while lis:
                v1, v2 = lis[-1], lis[-1] - diff
                l1.add(v1)
                lis.remove(v1)
                if v2 in lis:
                    l2.add(v2)
                    lis.remove(v2)
                else:
                    return []


            if diff in l1 and 0 in l2 and (x := solve(left - 1, l2)):
                return [diff] + x
            if -diff in l2 and 0 in l1 and (x := solve(left - 1, l1)):
                return [- diff] + x
            return []
            
        return solve(n, SortedList(sums))
                
        
