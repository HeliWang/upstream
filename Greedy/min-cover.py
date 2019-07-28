"""
    Find Minimum Cover
    https://www.1point3acres.com/bbs/thread-516692-1-1.html
    Greedy, similar to MST
    https://repl.it/repls/FluffyJampackedInternalcommand

    Given a list of continuous ranges,
    e.g. A = [[1, 3], [2, 4], [4, 5], [5, 6], [2, 6]]
    The minimum cover of A is [[1,3], [2, 6]]

    Idea:
    Assume the given input A can form a cover
    Sort A by left bound of each pair.

    If multiple pairs have same left bound in A, only keep one pair with the maximum right bound and filter everything out.

    Let pointer i initially point to A[0]
    Global Variable res is the current result list of pairs, initially A[0]
    Global Variable res_upper is the maximum right point of pairs in res, initially A[0][1]

    Each time move i forward as far as possible so that A[i] <= res_upper, record the pair during the movement with the max right bound, noted as A[j]
    Add new A[j] to res and update res_upper as A[j][1]
"""

def min_cover(A):
    assert A
    A.sort()
    A_copy, A = list(A), []
    # If multiple pairs have same left bound in A,
    #   only keep one pair with the maximum right bound and filter everything out.
    for i, pair in enumerate(A_copy):
        k, v = pair
        if not A or A[-1][0] != k:
            A.append(pair)
        else:
            A[-1] = pair
    res = [A[0]] #  the current result list of pairs
    res_upper = A[0][1] # the maximum right point of pairs in res
    i = 0
    while i < len(A):
        j = -1
        while i < len(A) and A[i][0] <= res_upper:
            if j == -1 or A[j][1] < A[i][1]:
                j = i
            i += 1
        if j != -1:
            if res_upper < A[j][1]:
                res.append(A[j])
                res_upper = A[j][1]
            else:
                break
    return res

print(min_cover([[1, 3], [2, 4], [4, 5], [5, 6], [2, 6]]))