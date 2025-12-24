class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)

        used = 0
        current = 0

        for c in capacity:
            current += c
            used += 1
            if current >= total_apples:
                return used
