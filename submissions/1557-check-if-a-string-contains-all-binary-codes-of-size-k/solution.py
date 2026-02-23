class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:


        t = { 'cnt': 0 }
        def insert(word, tt):
            if not word:
                tt['cnt'] = 1
                return

            if word[0] not in tt:
                tt[word[0]] = {'cnt': 0}
            insert(word[1:], tt[word[0]])
            tt['cnt'] = tt.get('0', {'cnt': 0})['cnt'] + tt.get('1', {'cnt': 0})['cnt']
        
        curr = ''
        for c in s:
            if t['cnt'] == 2 ** k:
                break
            curr += c
            if len(curr) > k:
                curr = curr[1:]
            if len(curr) == k:
                insert(curr, t)


        return t['cnt'] == 2 ** k
            

            
        
