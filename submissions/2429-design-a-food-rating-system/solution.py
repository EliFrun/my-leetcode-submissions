class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {
            food: cuisine for food, cuisine in zip(foods, cuisines)
        }

        self.ratings = {
            food: rating for food,rating in zip(foods, ratings)
        }

        self.cuisines = defaultdict(SortedList)
        for cuisine, rating, food in zip(cuisines,ratings, foods):
            self.cuisines[cuisine].add((rating, food))
        

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foods[food]
        rating = self.ratings[food]
        self.cuisines[cuisine].remove((rating, food))
        self.cuisines[cuisine].add((newRating, food))
        self.ratings[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        rating = self.cuisines[cuisine][-1][0]
        idx = self.cuisines[cuisine].bisect_left((rating, ''))
        return self.cuisines[cuisine][idx][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
