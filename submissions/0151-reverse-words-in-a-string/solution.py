class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        ret = ''
        for word in reversed(words):
            if word != ' ' and word != '':
                ret += f'{word.strip()} '
                
        return ret[:-1]
