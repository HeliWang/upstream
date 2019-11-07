class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        [0,1,0,2,1,0,1,3,2,1,2,1]
         ^i
                               ^j
           ^i
                               ^j
        """
        if not height:
            return 0
        area = 0
        i = 0
        j = len(height) - 1
        mh_l = 0
        mh_r = 0
        vi = height[i]
        vj = height[j]
        while i < j:
            mh_l = max(mh_l, vi)
            mh_r = max(mh_r, vj)
            if mh_l < mh_r:
                area += (mh_l - vi)
                i += 1
                vi = height[i]
            else:
                area += (mh_r - vj)
                j -= 1
                vj = height[j]
        return area
