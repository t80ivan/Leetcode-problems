"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.



Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
"""


class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def recur(words, chars, pos):
            result = []
            for i in words:
                new_words = [i[:pos] + chars[0] + i[pos + 1:], i[:pos] + chars[1] + i[pos + 1:]]
                for w in new_words:
                    result.append(w)
            return result

        result = [s]
        for i in range(len(s)):
            if s[i].isalpha():
                result = recur(result, [s[i].lower(), s[i].upper()], i)
        return result
