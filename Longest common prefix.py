Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            s1, s2 = max(strs), min(strs)
            i, match = 0, 0
            while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
                i, match = i+1, match + 1
            return s1[0:match]
