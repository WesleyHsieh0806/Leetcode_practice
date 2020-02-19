class Solution:
    def isPalindrome(self, x: int) -> bool:
        input = str(x)
        if x < 0:
            return False
        for i in range(0, len(input)):
            if input[i] != input[-1-i]:
                return False
        return True
