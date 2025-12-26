class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # initial penalty = all Y customers (if closed at 0)
        penalty = customers.count('Y')
        min_penalty = penalty
        best_hour = 0
        
        for i, ch in enumerate(customers):
            if ch == 'Y':
                penalty -= 1   # this Y is now served (good)
            else:
                penalty += 1   # this N becomes an empty open hour (bad)
            
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1
        
        return best_hour
