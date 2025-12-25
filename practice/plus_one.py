class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range (len(digits)-1,-1,-1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0
        return [1] + digits

print(Solution().plusOne([1,2,3,4,5,6,7,8,9]))