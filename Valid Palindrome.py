class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for char in s:
            if char.isalnum():
                newS += char.lower()
        rev = newS[::-1]
        if rev == newS:
            return True
        else:
            return False
