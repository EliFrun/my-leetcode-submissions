class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        if len(s) == 1:
            if s <= target:
                return ''
            return s

        c = Counter(s)
        if len([x for x in c.values() if x & 1]) > 1:
            return ''

        # can make palindrome
        def solve(left_higher, right_higher, letters):
            nonlocal odd
            if left_higher:
                return letters

            if len(letters) == 1:
                if letters[0] > target[len(target)//2-1]:
                    return letters[0]
                if letters[0] < target[len(target)//2-1]:
                    return ''
                if len(target) & 1 == 1:
                    if target[len(target)//2] > odd:
                        return ''
                    if target[len(target)//2] < odd:
                        return letters[0]
                if letters[0] > target[-(len(target)//2)]:
                    return letters[0]
                if letters[0] < target[-(len(target)//2)]:
                    return ''
                return letters[0] if right_higher else ''
            
            for i in range(len(letters)):
                if i < len(letters) - 1 and letters[i + 1] == letters[i]:
                    continue
                if letters[i] < target[len(target)//2 - len(letters)]:
                    continue
                elif letters[i] > target[len(target)//2 - len(letters)]:
                    return letters[i] + solve(True, True, letters[:i] + letters[i + 1:])
                else:
                    if letters[i] > target[ - (len(target)//2) + len(letters) - 1]:
                        right_higher = True
                    if letters[i] < target[ - (len(target)//2) + len(letters) - 1]:
                        right_higher = False
                    v = solve(False, right_higher, letters[:i] + letters[i+1:])
                    if v:
                        return letters[i] + v
            return ''
        
        
        l = []
        odd = ''
        for k,v in c.items():
            l.append(k * (v//2))
            if v & 1:
                odd = k

        l = ''.join(sorted(l))
        res = solve(False, False, l)
        if not res:
            return ''
        return res + odd + res[::-1]

                
                    
                
        
