"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        ")()())" -> 4
        "((()()())" -> 8
        "()(()" -> 2
        "()(())"
        "()(()(()"
        "()(()(())"
        "()(()(()))"
        "()(()(())))"
        """
        # 41m07s7
        longest = 0
        stack = [-1]  # storing the start point (exclusive) of valid parentheses substr
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack[-1] != -1 and s[stack[-1]] == '(':
                    stack.pop()
                    longest = max(i - stack[-1], longest)
                else:
                    stack.append(i)
        return longest
