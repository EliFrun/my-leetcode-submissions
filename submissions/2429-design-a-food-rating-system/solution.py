class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.d = defaultdict(SortedList)
        self.f = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
           self.d[cuisine].add([-rating, food])
           self.f[food] = [cuisine, -rating]

        

    def changeRating(self, food: str, newRating: int) -> None:
        self.d[self.f[food][0]].remove([self.f[food][1], food])
        self.d[self.f[food][0]].add([-newRating, food])
        self.f[food][1] = -newRating
        

    def highestRated(self, cuisine: str) -> str:
        return self.d[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
