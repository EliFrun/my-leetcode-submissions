class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_map = defaultdict(set)
        wordList.extend([beginWord])
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        for word in wordList:
            opts = 'abcdefghijklmnopqrstuvwxyz'
            for i in range(len(word)):
                for c in opts:
                    foo = ''.join(word[:i] + c + word[i + 1:])
                    if foo == word:
                        continue
                    if foo in wordList:
                        word_map[word].add(foo)
                        word_map[foo].add(word)

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
        
