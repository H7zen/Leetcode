class Solution(object):
    def romanToInt(self, s):
        sl = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        total = 0
        value = 0
        for num in reversed(s):
            current = sl[num]
            if current < value:
                total -= current
            else:
                total += current
            value = current
        return total
#can't lie I cheated
