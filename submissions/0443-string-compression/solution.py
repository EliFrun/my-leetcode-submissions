class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = chars[0]
        count = 1
        ret = []
        for c in chars[1:]:
            if c == curr:
                count += 1
            else:
                ret.append(curr)
                if count > 1:
                    ret.extend(list(str(count)))
                curr = c
                count = 1
        ret.append(curr)
        if count > 1:
            ret.extend(list(str(count)))


        i = 0
        while i < len(ret):
            if i < len(chars):
                chars[i] = ret[i]
            else:
                chars.append(ret[i])

            i += 1

        while len(chars) > len(ret):
            chars.pop()

        return len(chars)

        
