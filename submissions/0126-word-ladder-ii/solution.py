class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.extend([beginWord])
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        
        
        word_map = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    foo = ''.join(word[:i] + c + word[i + 1:])
                    if foo == word:
                        continue
                    if foo in wordList:
                        word_map[word].add(foo)
                        word_map[foo].add(word)

        def min_depth():
            visited = set()
            curr = set([beginWord])
            counter = 0
            while curr:
                counter += 1
                nxt = set()
                for word in curr:
                    if word == endWord:
                        return counter
                    visited.add(word)
                    candidates = word_map[word]
                    nxt = nxt.union(candidates)
                curr = nxt.difference(visited)

            return 0

        min_depth = min_depth()

        @functools.cache
        def dfs(word, depth):
            nonlocal min_depth
            nonlocal word_map
            if depth > min_depth:
                return []

            if depth == min_depth:
                return [[word]] if word == endWord else []

            ret = []
            for w in word_map[word]:
                #if w in visited:
                #    continue
                ret.extend(
                    dfs(
                        #visited.union(set([w])),
                        w,
                        depth + 1
                    )
                )
            return [[word] + r for r in ret if len(r) > 0]
            

        return dfs( beginWord, 1)
        
