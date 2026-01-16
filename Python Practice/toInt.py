class Solution:
    def toIntager(self, roman_num):
        roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        total = 0
        n = len(roman_num)

        for i in range(n):
            value = roman_map[roman_num[i]]
            if i + 1 < n and value < roman_map[roman_num[i + 1]]:
                total -= value
            else:
                total += value
        return total


print(Solution().toIntager(""))


