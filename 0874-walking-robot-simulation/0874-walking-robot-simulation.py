class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
      
        # Store obstacles in a set for fast lookup
        obstacle_set = set(map(tuple, obstacles))
        
        # Directions: North, East, South, West
        directions = [
            (0, 1),   # North
            (1, 0),   # East
            (0, -1),  # South
            (-1, 0)   # West
        ]
        
        x, y = 0, 0
        direction = 0
        max_distance = 0
        
        for cmd in commands:
            
            if cmd == -1:
                # Turn right
                direction = (direction + 1) % 4
                
            elif cmd == -2:
                # Turn left
                direction = (direction + 3) % 4
                
            else:
                # Move forward step by step
                dx, dy = directions[direction]
                
                for _ in range(cmd):
                    nx = x + dx
                    ny = y + dy
                    
                    if (nx, ny) in obstacle_set:
                        break
                    
                    x, y = nx, ny
                    
                    # Update max squared distance
                    max_distance = max(
                        max_distance,
                        x * x + y * y
                    )
        
        return max_distance