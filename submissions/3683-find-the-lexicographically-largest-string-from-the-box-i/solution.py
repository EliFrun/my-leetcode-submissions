class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        d = defaultdict(list)
        for i in range(len(word)):
            d[word[i]].append(i)

        best = max(d.keys())
        ret = ""
        for i in d[best]:
            ret = max(ret, word[i:len(word) + i - numFriends + 1])
        return ret
