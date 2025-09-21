class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # price lookup
        self.price = {}
        for shop, movie, p in entries:
            self.price[(shop, movie)] = p

        # unrented movies per movieId
        self.unrented = {}
        for shop, movie, p in entries:
            if movie not in self.unrented:
                self.unrented[movie] = SortedList()
            self.unrented[movie].add((p, shop))

        # global rented list
        self.rented = SortedList()

    def search(self, movie: int) -> List[int]:
        if movie not in self.unrented:
            return []
        # return up to 5 cheapest shops for this movie
        return [shop for _, shop in self.unrented[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        # remove from unrented
        self.unrented[movie].remove((p, shop))
        # add to rented
        self.rented.add((p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        # remove from rented
        self.rented.remove((p, shop, movie))
        # add back to unrented
        self.unrented[movie].add((p, shop))

    def report(self) -> List[List[int]]:
        # return up to 5 cheapest rented movies
        return [[shop, movie] for p, shop, movie in self.rented[:5]]

        
# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()