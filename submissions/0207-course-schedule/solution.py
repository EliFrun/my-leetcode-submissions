class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_deps = [[] for i in range(numCourses)]
        can_reach_base = [0 for i in range(numCourses)]
        
        for c, p in prerequisites:
            course_deps[c].append(p)
            
        def dfs(c):
            nonlocal can_reach_base
            if can_reach_base[c] == -1:
                return False
            if can_reach_base[c] == 1:
                return True
            
            nonlocal course_deps
            for p in course_deps[c]:
                can_reach_base[c] = -1
                if not dfs(p):
                    return False
                can_reach_base[c] = 1
                
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
                
            
        
        
