class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # List to store number of devices in each non-empty row
        device_counts = []
        
        for row in bank:
            count = row.count('1')
            if count > 0:
                device_counts.append(count)
        
        total_beams = 0
        
        # Calculate beams between consecutive non-empty rows
        for i in range(1, len(device_counts)):
            total_beams += device_counts[i - 1] * device_counts[i]
        
        return total_beams
        