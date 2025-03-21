class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ing_map = {}
        for r, i in zip(recipes, ingredients):
            ing_map[r] = i
        
        c = {}

        supplies = set(supplies)
        def solve(r, visited):
            if r in visited:
                c[r] = False

            if r in c:
                return c[r]

            if r not in ing_map:
                c[r] = r in supplies
                return c[r]
            
            for d in ing_map[r]:
                if not solve(d, visited.union(set([r]))):
                    c[r] = False
                    return False
            c[r] = True
            return True

        ret = []
        for r in recipes:
            if solve(r, set()):
                ret.append(r)

        print(dict(ing_map))
        print(c)

        return ret
        
