class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # find if any node has in-degree == 2
        indegree = defaultdict(list)
        bad_node = 0
        for p, c in edges:
            indegree[c].append(p)
            if len(indegree[c]) == 2:
                bad_node = c

        def parent_set(node):
            ret = set()
            curr = node
            while curr:
                if curr in ret:
                    return False
                ret.add(curr)
                curr = indegree[curr][0] if len(indegree[curr]) > 0 else None
            
            return ret
        
        if bad_node > 0:
            candidates = [
                indegree[bad_node][0],
                indegree[bad_node][1]
            ]
            a = indegree[bad_node].pop(1)
            set_left = parent_set(a)
            set_right = parent_set(bad_node)
            if set_left == False or set_right == False:
                return [candidates[0], bad_node]
            if len(set_left.intersection(set_right)) > 0:
                return [candidates[1], bad_node]
            return [candidates[0], bad_node]

        # find cycle remove right most entry
        # @functools.cache
        def highest_parent(node):
            nonlocal visited
            if node in visited:
                return node
            visited.add(node)
            if len(indegree[node]) > 0:
                return highest_parent(indegree[node][0])
            return node

        for p, c in edges[::-1]:
            visited = set()
            a = highest_parent(c)
            if a == c:
                return [p, c]
                
            



        
        
