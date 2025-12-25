class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
            elif num > target:
                return i
        return len(nums)


print(Solution().searchInsert([1, 4, 6, 8], 3))



