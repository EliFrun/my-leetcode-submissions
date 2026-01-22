class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        s = SortedList(list(enumerate(nums)))
        bad_indexes = set()
        q = []
        for i in range(len(s) - 1):
            heappush(q, (s[i + 1][1] + s[i][1], i))
            if s[i][1] > s[i + 1][1]:
                bad_indexes.add(i)

        cnt = 0
        while bad_indexes:
            d, ii = heappop(q)
            i = s.bisect_left((ii, float('-inf')))
            if i >= len(s) - 1:
                continue
            if s[i][0] != ii:
                continue
            if s[i][1] + s[i + 1][1] != d:
                continue
            idx, v = s.pop(i)
            if idx in bad_indexes:
                bad_indexes.remove(idx)
            idx2, v2 = s.pop(i)
            if idx2 in bad_indexes:
                bad_indexes.remove(idx2)
            v += v2
            s.add((idx, v))
            if i > 0:
                if s[i][1] < s[i - 1][1]:
                    bad_indexes.add(s[i - 1][0])
                else:
                    if s[i - 1][0] in bad_indexes:
                        bad_indexes.remove(s[i - 1][0])
                heappush(q, (s[i - 1][1] + s[i][1], s[i - 1][0]))
            if i < len(s) - 1:
                if s[i][1] > s[i + 1][1]:
                    bad_indexes.add(s[i][0])
                heappush(q, (s[i][1] + s[i + 1][1], s[i][0]))
            cnt += 1

        return cnt
        
