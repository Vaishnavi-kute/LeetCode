class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 0  # slow pointer
        
        for j in range(1, len(nums)):  # fast pointer
            if nums[j] != nums[i]:     # found a new unique element
                i += 1
                nums[i] = nums[j]      # place it at the next unique position
        
        return i + 1  # count of unique elements
