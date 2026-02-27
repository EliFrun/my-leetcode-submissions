class Solution:
    def minOperations(self, s: str, k: int) -> int:
        curr = set([len(s)])

        lists = [SortedList(range(len(s)- 1, -1, -2)), SortedList(range(len(s), -1, -2))]

        d = {}

        counts = defaultdict(int)

        cnt = 0
        while curr:
            nxt = set()
            opts = lists[cnt & 1] if k & 1 else lists[1]
            for v in curr:
                counts[v] += 1
                d[v] = cnt
                ones = v
                zeroes = len(s) - ones
                max_ones = min(ones, k)
                max_zeroes = min(zeroes, k)
                left_bound = ones - max_ones + (k - max_ones)
                right_bound = ones + max_zeroes - (k - max_zeroes)
                l = set()
                for i in range(opts.bisect_left(left_bound), opts.bisect_right(right_bound)):
                    if (opts[i] - v) & 1 == (k & 1):
                        l.add(opts[i])


                for j in l:
                    opts.remove(j)

                nxt |= l
            curr = nxt
            cnt += 1


        d[len(s)] = 0
        return d.get(s.count('1'), -1)
            
