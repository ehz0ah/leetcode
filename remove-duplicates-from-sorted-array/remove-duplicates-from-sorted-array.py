class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    '''
    make a slow pointer that points at the 0th index and a fast pointer at the 1st index
    the slow pointer will increment only when the slow and fast pointer points at different objects
    the fast pointer will iterate through the array to look for new unique elemnets
    '''
    slow , fast = 0 , 1
    while fast in range(len(nums)):
      if nums[slow] == nums[fast]:
        fast += 1
      else:
        nums[slow + 1] = nums[fast]
        fast += 1
        slow += 1
    return slow + 1
