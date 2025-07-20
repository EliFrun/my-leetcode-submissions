class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        trie = {}
        for path in paths:
            curr = trie
            for d in path:
                if d not in curr:
                    curr[d] = {}
                curr = curr[d]


        d = {}
        def encode_dirs(prev_path, node):
            if not node:
                return [[]]
            
            ret = []
            for key in node.keys():
                ret.extend([[key] + x for x in encode_dirs(tuple(list(prev_path) + [key]), node[key])])
            d[prev_path] = tuple(sorted(tuple(x) for x in ret))
            return ret

        encode_dirs((), trie)

        counts = defaultdict(list)
        for key, value in d.items():
            counts[value].append(key)

        bad_paths = [v for v in counts.values() if len(v) > 1]
        for lis in bad_paths:
            for path in lis:
                curr = trie
                for i, d in enumerate(path):
                    if i == len(path) - 1:
                        curr.pop(d)
                    else:
                        if d not in curr:
                            break
                        curr = curr[d]

        def full_paths(node):
            if not node:
                return [[]]
            
            ret = []
            for key in node.keys():
                ret.append([key])
                ret.extend([[key] + x for x in full_paths(node[key])])

            return ret

        return [list(x) for x in set([tuple(y) for y in full_paths(trie)]) if x]

        



            



        
