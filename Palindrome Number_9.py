class Solution(object):
    def isPalindrome(self, x):
        a = list(str(x))
        b = list(str(x))
        b.reverse()
        if a == b:
            return True
        else:
            return False
