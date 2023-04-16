class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums:
                remainder_index = nums.index(remainder)
                if remainder_index != i:
                    return [remainder_index,i]