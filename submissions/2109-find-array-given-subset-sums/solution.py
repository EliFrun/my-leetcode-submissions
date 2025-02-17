class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        def solve(t, s, m):
            if m == 1:
                return [t]
            
            if (diff := s[-1] - s[-2]) in s:
                lis = s.copy()
                with_num = SortedList()
                without_num = SortedList()
                while lis:
                    if lis[-1] - diff in s:
                        with_num.add(lis[-1])
                        without_num.add(lis[-1] - diff)
                        lis.remove(lis[-1] - diff)
                        lis.remove(lis[-1])
                    else:
                        break
                if not lis:
                    if res := solve(t - diff, without_num, m - 1):
                        return [diff] + res
            if (diff := s[-2] - s[-1]) in s:
                lis = s.copy()
                with_num = SortedList()
                without_num = SortedList()
                while lis:
                    if lis[0] - diff in s:
                        with_num.add(lis[0])
                        without_num.add(lis[0] - diff)
                        lis.remove(lis[0] - diff)
                        lis.remove(lis[0])
                    else:
                        break
                if not lis:
                    if res := solve(t - diff, without_num, m - 1):
                        return [diff] + res

            return []
            
        
        target = sum(sums) // (2 ** (n - 1))
        return solve(target, SortedList(sums), n)
        
