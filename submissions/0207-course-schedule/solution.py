class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cache = ['not_visited'] * numCourses
        deps = [[] for _ in range(numCourses)]
        
        for p in prerequisites:
            deps[p[0]].append(p[1])
            
        def dfs(course):
            nonlocal cache
            nonlocal deps
            if cache[course] == 'safe':
                return True
            if cache[course] == 'visited':
                return False
            if not deps[course]:
                cache[course] = 'safe'
                return True
            
            cache[course] = 'visited'
            for dep in deps[course]:
                if not dfs(dep):
                    return False
                
            cache[course] = 'safe'
                
            return True
        
        print(deps)
        print(cache)
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
        
        
