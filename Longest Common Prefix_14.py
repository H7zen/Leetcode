class Solution(object):
    def longestCommonPrefix(self, strs):
        chars = []
        first_w = strs[0]

        for i in range(len(first_w)):
            current_char = first_w[i]

            for word in strs[1:]:
                if i >= len(word) or word[i] != current_char:
                    return ''.join(chars)

            chars.append(current_char)

        return "".join(chars)  
