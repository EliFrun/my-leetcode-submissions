class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        for l in 'abcdefghijklmnopqrstuvwxyz':
            for c in key:
                if c == ' ':
                    continue
                if c not in d:
                    d[c] = l
                    break


        return ''.join([d[x] if x != ' ' else ' ' for x in message])
        
