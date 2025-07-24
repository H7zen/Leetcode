class Solution(object):
    def longestCommonPrefix(self, strs):
        chars = []
        strs.sort()
        first_w = strs[0]
        last_w = strs[-1]

        for i in range(len(first_w)):
            current_char = first_w[i]
            
            if first_w[i] != last_w[i]:
                return "".join(chars)

            chars.append(current_char)
        return "".join(chars)
