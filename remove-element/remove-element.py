class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for inte in nums:
            if inte != val:
                nums[index] = inte
                index +=1 
        return index
        
       