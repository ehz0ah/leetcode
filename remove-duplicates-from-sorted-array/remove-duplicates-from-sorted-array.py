class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        nums =  doesn't replace elements in the original list.
        nums[:] = replaces element in place
        '''
        nums[:] = sorted(set(nums))
        return len(nums)
        

