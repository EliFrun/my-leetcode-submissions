class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        for word in folder:
            word = word[1:].split('/')
            curr = trie
            for d in word:
                if d not in curr:
                    curr[d] = {}
                curr = curr[d]

        for word in folder:
            word = word[1:].split('/')
            curr = trie
            for d in word:
                curr = curr.get(d, {})
            for key in list(curr.keys()):
                curr.pop(key)


        def solve(curr):
            if not curr:
                return ['']
            ret = []
            for key in curr.keys():
                ret.extend('/' + key + x for x in solve(curr[key]))
            return ret
        return solve(trie)

