class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool

        str1 = "aabccdd",
        str2 = "ccceecc",

        Both str1 and str2 contain only lowercase English letters.

        seq of the transformation matters!
        for example, the following will not be valid
        "abcdefghijklmnopqrstuvwxyz"
        "bcdefghijklmnopqrstuvwxyza"
        """
        n = len(str1)
        if n != len(str2):
            return False
        transform_map = {}
        for i, c in enumerate(str1):
            if c in transform_map and transform_map[c] != str2[i]:
                return False
            transform_map[c] = str2[i]
        num_diff_mapping = len(filter(lambda x: x[0] != x[1], transform_map.items()))
        num_keys = len(transform_map.keys())
        num_vals = len(set(transform_map.values()))
        return not (num_keys == 26 and num_vals == 26 and num_diff_mapping >= 1)
