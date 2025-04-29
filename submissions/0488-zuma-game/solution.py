class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        @cache
        def prune(b,h):
            b = Counter(b)
            h = Counter(h)
            for k,v in b.items():
                if v < 3 and h.get(k, 0) + v < 3:
                    return True
            return False

        def simplify(b, i):
            ret_left, ret_right = i - 1, i
            left, right = i - 1, i + 1
            curr = b[i]
            count = 1
            while True:
                while True:
                    if left >= 0 and b[left] == curr:
                        count += 1
                        left -= 1
                    else:
                        break
                
                while True:
                    if right < len(b) and b[right] == curr:
                        count += 1
                        right += 1
                    else:
                        break

                if count > 2:
                    count = 0
                    ret_left, ret_right = left, right
                    if left >= 0 and right < len(b) and b[left] == b[right]:
                        curr = b[left]
                else:
                    break
            return b[:ret_left + 1] + b[ret_right:]
            
      
        hand = ''.join(sorted(hand))
        curr = [(board, hand)]
        layer = -1
        while curr:
            layer += 1
            nxt = []
            seen = set()
            for b, h in curr:
                if prune(b,h):
                    continue
                if not b:
                    return layer
                for i, l in enumerate(h):
                    if i < len(h) - 1 and h[i] == h[i + 1]:
                        continue
                    for j in range(len(b) + 1):
                        if j < len(b) - 1:
                            if b[j] == b[j + 1]:
                                continue
                            # lines 61 - 68 somehow increase speed by 90%
                            skip = True
                            if b[j] == b[j + 1]:
                                skip = False
                            if b[j] == l or b[j + 1] == l:
                                skip = False
                            if skip:
                                continue
                        left = b[:j]
                        right = b[j:]
                        board_state = simplify(left + l + right, j)
                        hand_state =  h[:i] + h[i + 1:]
                        if (board_state, hand_state) in seen:
                            continue
                        seen.add((board_state, hand_state))
                        nxt.append((board_state, hand_state))
            
            curr = nxt

        return -1

        
