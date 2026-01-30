class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g = defaultdict(list)

        for o,c,co in zip(original,changed,cost):
            g[o].append((c, co))

        dp = defaultdict(lambda: defaultdict(lambda:1e12))
        for word in list(g.keys()):
            q = [(0, word)]
            layer = defaultdict(lambda:1e12)
            while q:
                d, w = heappop(q)
                if layer[w] <= d:
                    continue
                layer[w] = d
                for c, co in g[w]:
                    heappush(q, (d + co, c))


            dp[word] = layer


        t = {}
        for word in dp.keys():
            curr = t
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['word'] = word


        dp2 = [1e12] * (len(source) + 1)
        dp2[-1] = 0
        prev_words = []
        for i in range(len(source)):
            prev_words = [x[source[i]] for x in prev_words if source[i] in x]
            if source[i] in t:
                prev_words.append(t[source[i]])
            if source[i] == target[i]:
                dp2[i] = min(dp2[i], dp2[i - 1])

            for x in prev_words:
                if 'word' not in x:
                    continue
                word = x['word']
                dp2[i] = min(dp2[i], dp2[i - len(word)] + dp[word][target[i - len(word) + 1: i + 1]])

        return dp2[-2] if dp2[-2] != 1e12 else -1
            


            
        
