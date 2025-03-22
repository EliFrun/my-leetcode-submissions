class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        i = 0
        while i < len(asteroids) and mass >= asteroids[i]:
            mass += asteroids[i]
            i += 1
        return i >= len(asteroids)
        
