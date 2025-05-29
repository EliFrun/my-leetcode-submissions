class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_map = {}
        for i,v in enumerate(req_skills):
            skill_map[v] = i

        req_skills = [i for i in range(len(req_skills))]

        for person in people:
            for i in range(len(person)):
                person[i] = skill_map[person[i]]

        for i in range(len(people)):
            people[i] = set(people[i])

        @cache
        def solve(needed, i):
            if len(needed) == 0:
                return []
            if i >= len(people):
                return [0] * len(people)
            s_n = set(needed) - people[i]

            ret_1 = [i] + solve(tuple(sorted(list(s_n))), i + 1)
            ret_2 = solve(needed, i + 1)
            if len(ret_1) < len(ret_2):
                return ret_1
            return ret_2

        return solve(tuple(req_skills), 0)


            
            

