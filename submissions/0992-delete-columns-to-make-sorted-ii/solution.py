class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        curr_strings = [''] * len(strs)
        ret = 0
        for i in range(len(strs[0])):
            nxt_strings = [x + strs[j][i] for j,x in enumerate(curr_strings)]
            to_delete = False
            strictly_less = True
            for i in range(len(nxt_strings) - 1):
                if nxt_strings[i] < nxt_strings[i + 1]:
                    continue
                elif nxt_strings[i] <= nxt_strings[i + 1]:
                    strictly_less = False
                else:
                    to_delete = True

            if to_delete:
                ret += 1
            elif strictly_less:
                return ret
            else:
                curr_strings = nxt_strings
        return ret

