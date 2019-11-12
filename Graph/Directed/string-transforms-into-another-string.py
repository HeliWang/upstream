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
        should be False

        "abcdefghijklmnopqrstuvwxyz"
        "abcdefghijklmnopqrstuvwxyz"
        should be True

        "abcdefghijklmnopqrstuvw"
        "bcdefghijklmnopqrstuvwx"
        should be True

        Model the problem as a graph problem.
        Add an edge from one character to another if you need to convert between them.
        What if one character needs to be converted into more than one character?
        There would be no solution. Thus, every node can have at most one outgoing edge.
        How to process a cycle?

        It is not possible to convert x directly to y when y is also in str1
        however, if there is any spare char not used in str1, then we can convert x to z, then z to y
        thus, only when len(str1) == 26, then there is no spare char in str1.

        However, even len(str1) == 26, we may be able to convert:
          two distinct chars in str1 convert to the same char in str2
          first convert the two dist chars to the same char in str2, then there is a spare char available in str1

        However, we also need to consider the corner case:
          all char in str1 convert to the same char to str2
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