class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        one, two = 0, 1,
        while two <= len(nums) - 1:
            if nums[one] != nums[two]:
                one += 1
                two += 1
            elif nums[one] == nums[two] and two - one >= 2:
                nums.remove(nums[two])
            else:
                two += 1
        return len(nums)

            
