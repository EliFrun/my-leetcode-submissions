class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        binary_encodings = []
        for row in seats:
            opts = [0]
            if row[0] == ".":
                opts.append(1)
            for i in range(1, len(row)):
                if row[i] == '#':
                    continue
                nxt = []
                for opt in opts:
                    if not (opt >> (i - 1) & 1):
                        nxt.append(opt | (1 << i))
                    nxt.append(opt)
                opts = nxt
            binary_encodings.append(opts)
        
        @cache
        def solve(row, prev):
            if row >= len(binary_encodings):
                return 0
            
            ret = 0
            for enc in binary_encodings[row]:
                cnt = 0
                can_test = True
                for i in range(len(seats[0])):
                    if (enc >> i) & 1:
                        if ((prev >> (i - 1) if i - 1 >= 0 else 0) & 1) | ((prev >> (i + 1)) & 1):
                            can_test = False
                            break
                        cnt += 1

                if can_test:
                    ret = max(ret, cnt + solve(row + 1, enc))

            return ret

        return solve(0, 0)
