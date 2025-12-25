class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sum = []
        indices = [i for i, x in enumerate(nums) if x == 3]
        pairs = [(i, j) for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] == nums[j] == 3]
        for pair in pairs:
             for pair2 in pairs:
                 sum.append(pair2[0] + pair2[1] + pair2[2])
        return sum
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))