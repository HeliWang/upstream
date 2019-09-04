# https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    # Way 1:  find the last number which is greater than num
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}

        stack = []  # mono stack max -> min
        # [1, 3, 4, 2, 5]
        for num in nums2[::-1]:
            while stack and stack[-1] < num:
                stack.pop()
            if stack:
                next_greater[num] = stack[-1]
            stack.append(num)
        return [next_greater.get(num, -1) for num in nums1]

    # Way 2:  find the next number which is greater than num
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}

        stack = []  # mono stack max -> min
        # [1, 3, 4, 2, 5]
        for num in nums2:
            while stack and stack[-1] < num:
                n = stack.pop()
                next_greater[n] = num
            stack.append(num)
        return [next_greater.get(num, -1) for num in nums1]


# https://leetcode.com/problems/next-greater-element-ii/
"""
Given a circular array (the next element of the last element
 is the first element of the array), print the Next Greater
  Number for every element. The Next Greater Number of a number
   x is the first greater number to its traversing-order next in the array,
    which means you could search circularly to find its next greater number. 
    If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
"""


class Solution(object):
    def nextGreaterElements(self, nums):
        res = [-1] * len(nums)
        stack = []  # an array of index. the values in nums of the indexes are max -> min
        for i, num in enumerate(nums + nums):
            while stack and nums[stack[-1]] < num:
                idx = stack.pop()
                res[idx] = num
            if i < len(nums):
                stack.append(i)
        return res


"""
Next Greater Node In Linked List
https://leetcode.com/problems/next-greater-node-in-linked-list/
"""


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        stack = []  # mono stack max -> min
        # [1, 3, 4, 2, 5]
        while head:
            num = head.val
            while stack and stack[-1][0].val < num:
                res[stack.pop()[1]] = num
            stack.append((head, len(res)))
            res.append(0)
            # since we don't know the len of the linked list, we can still place 0 into res when visited head
            head = head.next
        return res
