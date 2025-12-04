class Solution:
    def countCollisions(self, directions: str) -> int:
        # Remove leading L's (they never collide)
        i = 0
        while i < len(directions) and directions[i] == 'L':
            i += 1
        
        # Remove trailing R's (they never collide)
        j = len(directions) - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1
        
        # Count collisions for the middle part
        collisions = 0
        for k in range(i, j + 1):
            if directions[k] != 'S':
                collisions += 1
        
        return collisions

        