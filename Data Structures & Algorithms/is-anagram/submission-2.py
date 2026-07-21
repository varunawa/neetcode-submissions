class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort each string
        s_sort = ''.join(sorted(s))
        t_sort = ''.join(sorted(t))

        # go through each char in each string, as soon as different, return
        return s_sort == t_sort