class Solution:
    def countSubstrings(self, s: str) -> int:
        lists = []
        curr_lis = [s[0]]
        i = 1
        while i < len(s):
            if s[i] == curr_lis[0]:
                curr_lis.append(s[i])
            else:
                lists.append(''.join(curr_lis))
                curr_lis = [s[i]]

            i += 1

        lists.append(''.join(curr_lis))

        ret = 0
        for i, v in enumerate(lists):
            ret += (len(v) * (len(v) + 1)) // 2

            j = 1
            while (i - j) >= 0 and (i + j) < len(lists):
                left, right = lists[i - j], lists[i + j]
                if left[0] == right[0]:
                    ret += min(len(left), len(right))
                else:
                    break
                
                if len(left) == len(right):
                    j += 1
                else:
                    break

        print(lists)
        return ret
                    

            

