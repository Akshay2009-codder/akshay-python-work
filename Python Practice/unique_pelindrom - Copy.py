class Solution:
    def longestPalindrome(self, s: str) -> str:
        targate = []
        current = ""
        for char in s:
            if char in current:
                targate.append(current)
                current = ""
                current += char
            if current :
                targate.append(current)
        fainal = []
        length = 0
        for item in targate:
            if item == item[::-1]:
                fainal.append(item)
        for item in fainal:
            if len(item) > length:
                length = len(item)
                if length == 0:
                    return"no pelindrome in string"
        return length

print(Solution().longestPalindrome("babad"))


