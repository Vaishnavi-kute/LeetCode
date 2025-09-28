class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # position to place the next valid element
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # keep this element
                k += 1
        
        return k
