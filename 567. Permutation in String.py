"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def word_to_dict(word):
            wdict = {}
            for i in set(word):
                wdict[i] = word.count(i)
            return wdict

        s1dict = word_to_dict(s1)

        for i in range(len(s2) - len(s1) + 1):
            if s2[i] in s1dict.keys():
                s2dict = word_to_dict(s2[i:(i + len(s1))])
                if s2dict == s1dict:
                    return True
        return False
