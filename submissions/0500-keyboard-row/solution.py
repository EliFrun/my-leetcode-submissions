class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]

        d = {}
        for i, row in enumerate(rows):
            for c in row:
                d[c] = i


        ret = []
        for word in words:
            w = word
            word = word.lower()
            v = d[word[0]]
            insert = True
            for c in word[1:]:
                if d[c] != v:
                    insert = False
                    break

            if insert:
                ret.append(w)

        return ret
