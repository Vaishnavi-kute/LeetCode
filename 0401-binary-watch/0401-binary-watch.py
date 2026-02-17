class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for hour in range(12):          # hours: 0 to 11
            for minute in range(60):    # minutes: 0 to 59
                # Count total LEDs turned on
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    # Format minute with leading zero if needed
                    time = f"{hour}:{minute:02d}"
                    result.append(time)
        
        return result