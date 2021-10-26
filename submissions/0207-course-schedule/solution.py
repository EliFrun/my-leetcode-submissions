class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            courses[course].append(prereq)
            
        cache = ['not_visited' for _ in range(numCourses)]
            
            
        def dfs(course):
            nonlocal courses
            nonlocal cache
            
            if cache[course] == 'visited':
                return False
            if not courses[course]:
                return True
            if cache[course] == 'safe':
                return True
            
            cache[course] = 'visited'
            for prereq in courses[course]:
                if not dfs(prereq):
                    return False
            
            cache[course] = 'safe'
            
            return True
        
        return all([dfs(course) for course in range(numCourses)])
        
