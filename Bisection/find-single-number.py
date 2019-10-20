def find_single_num(nums):
    # [1]
    # [1, 2, 2]
    # [2, 2, 10, 10, 11]
    # [2, 2, 5, 5, 6, 10, 10]

    # [2, 2, 5, 5, 10, 10, 11]
    # [1, 2, 2, 5, 5, 10, 10] #
    # mid = (i + j) // 2

    # [1]
    # [1, 2, 2]
    # [1, 2, 2, 5, 5]
    # [1, 2, 2, 5, 5, 7, 7]

    # [10]
    # [2, 2, 10]
    # [2, 2, 5, 5, 10]
    # [2, 2, 5, 5, 7, 7, 10]

    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if l == mid:
            return nums[mid]
        if (r - l - 1) // 2 % 2 == 1:
            mid += 1
        if nums[mid - 1] == nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    print(l, r)


# print(find_single_num([2]))

print(find_single_num([1, 2, 2]))

# [1, 2, 2, 5, 5, 10, 10]

# print(find_single_num([2, 2, 11]))

# print(find_single_num([2, 2, 10, 10, 11]))

# print(find_single_num([2, 2, 10, 10, 11，11，12]))
