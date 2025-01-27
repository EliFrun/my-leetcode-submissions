class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parents = defaultdict(set)
        for pre, course in prerequisites:
            parents[course].add(pre)


        reachable = {}
        for i in range(numCourses):
            curr = set([i])
            visited = set()
            while curr:
                nxt = set()
                for n in curr:
                    if n in visited:
                        continue
                    visited.add(n)
                    if n in reachable:
                        visited = visited.union(reachable[n])
                    else:
                        nxt.update(parents[n])

                curr = nxt

            reachable[i] = visited

        return [pre in reachable[course] for pre, course in queries]


        
        
