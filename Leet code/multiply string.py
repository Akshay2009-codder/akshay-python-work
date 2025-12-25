class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        multiplection = (int(num1) * int(num2))
        return str(multiplection)
print(Solution().multiply("11", "22"))