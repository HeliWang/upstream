"""
    Find Minimum Cover
    https://www.1point3acres.com/bbs/thread-516692-1-1.html
    https://leetcode.com/problems/video-stitching/

    Given a list of continuous ranges,
    e.g. A = [[1, 3], [2, 4], [4, 5], [5, 6], [2, 6]]
    The minimum cover of A is [[1,3], [2, 6]]
"""

import sys


# greedy Solution of https://leetcode.com/problems/video-stitching
def videoStitching(clips, T):
    """
    :type clips: List[List[int]]
    :type T: int
    :rtype: int
    """
    clips.sort()  # (key = lambda x: (x[0], -x[1]))
    if not clips or clips[0][0] != 0: return -1
    low, high = 0, 0
    # [low, high] ends of selected clips,
    #   low is not necessary to record here
    count = 0  # nums of selected clips so far
    if high >= T: return count
    i = 0
    while i < len(clips):
        new_high = high
        # Each clip in clips is a [start, end] range
        # Go through the clip with start <= high
        #    and select the clip with max end value > current high among the clips
        while i < len(clips):
            if clips[i][0] > high:
                break
            new_high = max(new_high, clips[i][1])
            i += 1
        if new_high > high:
            count += 1
            high = new_high
            if high >= T: return count
        else:
            return -1
    return -1


# greedy Solution simplified version of https://leetcode.com/problems/video-stitching
def videoStitching(clips: List[List[int]], T: int) -> int:
    clips.sort()
    # lastEnd 是上一个clip的末尾，
    #    下一个clip的头（i）如果比lastEnd大，就得多一次拼接（ans+=1）
    # currEnd 是当前clip组合能到最远位置，
    #    有的时候不需要拼接也能扩大最远位置，把当前clip替换掉就行
    lastEnd, currEnd = -1, 0
    ans = 0
    for i, j in clips:
        if i > currEnd:
            return -1
        if lastEnd < i <= currEnd:
            ans += 1
            lastEnd = currEnd
        # if j <= lastEnd or lastEnd < j <= currEnd
        currEnd = max(j, currEnd)
        if currEnd >= T:
            return ans
    return -1


# DP Solution of https://leetcode.com/problems/video-stitching
def videoStitching(clips: List[List[int]], T: int) -> int:
    clips.sort()
    min_num_clip = [sys.maxsize] * (T + 1)
    if T == 0 and clips[0][0] == 0: return 1
    min_num_clip[0] = 0
    # [[0,2],[1,5],[1,9],[4,6],[5,9],[8,10]]
    for clip in clips:
        s, t = clip  # [s, t]
        # !!!!!!!!! IndexError: list index out of range !!!!!!!!!
        ### clips_required = [min_num_clip[i]
        ## for i in range(s, t) if i <= T]!!!! must be s
        if s > T: break
        required_clip_num = min_num_clip[s]
        for i in range(s + 1, t + 1):
            if i > T: break
            min_num_clip[i] = min(min_num_clip[i], required_clip_num + 1)
    if min_num_clip[T] == sys.maxsize: return -1
    return min_num_clip[T]
