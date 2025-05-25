class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        best_length = len(word) - numFriends + 1
        c = defaultdict(list)
        for i, v in enumerate(word):
            c[v].append(i)
        
        return max(word[idx: idx + best_length] for idx in c[max(c.keys())])
