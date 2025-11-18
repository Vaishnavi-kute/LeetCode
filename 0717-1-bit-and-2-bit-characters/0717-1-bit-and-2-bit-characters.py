#class Solution:
 #   def isOneBitCharacter(self, bits: List[int]) -> bool:



class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        Determine if the last character in the bit array must be a 1-bit character.
      
        Rules:
        - 1-bit character: represented as '0'
        - 2-bit characters: represented as '10' or '11'
      
        Args:
            bits: List of integers (0s and 1s) representing encoded characters
          
        Returns:
            True if the last character must be a 1-bit character, False otherwise
        """
        # Initialize pointer and get array length
        current_index = 0
        array_length = len(bits)
      
        # Process all characters except potentially the last one
        while current_index < array_length - 1:
            # If current bit is 0: it's a 1-bit character (move 1 position)
            # If current bit is 1: it's start of a 2-bit character (move 2 positions)
            # This works because bits[i] + 1 gives us:
            #   - 0 + 1 = 1 (move 1 position for 1-bit character)
            #   - 1 + 1 = 2 (move 2 positions for 2-bit character)
            current_index += bits[current_index] + 1
      
        # If we land exactly on the last position (array_length - 1),
        # it means the last bit forms a 1-bit character
        return current_index == array_length - 1
        