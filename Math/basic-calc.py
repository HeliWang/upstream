"""
Basic Calculator I (Hard)
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces.

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8) + 0 + 10000"
Output: 10023
"""


# Other People Version

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # https://leetcode.com/problems/basic-calculator/discuss/62361/Iterative-Java-solution-with-stack
        res, num = 0, 0
        sign = 1
        stack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in ["+", "-"]:
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0

        return res + sign * num


# My Version
class Sign:
    POS_VAL = 1
    NEG_VAL = -1

    def __init__(self, val):
        assert val == Sign.POS_VAL or val == Sign.NEG_VAL
        self.val = val


Positive = Sign(Sign.POS_VAL)
Negative = Sign(Sign.NEG_VAL)


def get_token(s, i):
    """
    :param s: exp
    :param i: start index
    :return: (token, len_token)
      token: int / Sign / parentheses ( or )
      len_token
    """
    assert i < len(s)
    if s[i] == "+":
        return Positive, 1
    if s[i] == "-":
        return Negative, 1
    if s[i] in ["(", ")"]:
        return s[i], 1
    token = 0
    len_token = 0
    while i < len(s) and s[i].isdigit():  # in "0123456789":  # please note i < len(s)!!!!!!!!
        token *= 10
        token += ord(s[i]) - ord('0')
        i += 1
        len_token += 1
    return token, len_token


def calculate(s):
    """
    :param s: A expression string which may contain open ( and closing parentheses ),
              the plus + or minus sign -,
              non-negative integers and empty spaces.
    empty spaces? What if 10 00?
    - 10000 + 0 - 20 + 10
    (( - (3 + 2) - (4 + 6)) + 3) - 20
    :return: value of the expression
    """
    s = s.replace(" ", "")
    res = 0
    sign = Positive
    stack = []  # (sign applying to the next level of (), val in current level)
    # e.g. ( 0 - (3 + 2) + 3) - 20
    # [(+1, 0), (-1, 0)]
    i = 0
    while i < len(s):
        token, len_token = get_token(s, i)
        if isinstance(token, Sign):
            sign = token
        elif isinstance(token, int):
            res += sign.val * token
        elif token == "(":
            stack.append((sign, res))
            res = 0  # create a new stack frame
            sign = Positive  # create a new stack frame
        elif token == ")":
            old_sign, old_res = stack.pop()
            res = old_res + old_sign.val * res  # restore stack frame
            sign = Positive  # restore stack frame
        i += len_token
    return res


assert calculate("1 + 1") == 2
assert calculate("10000 + 0 - 20") == 9980
assert calculate("(( - (3 + 2) - (4 + 6)) + 3) - 20") == -32

# Tests
"""
s = "(( - (3 + 2) - (4 + 6)) + 3) - 20"
i = 0
  token = (, len_token = 1
  stack  = [(+, 0)]
i = 1
  token = (, len_token = 1
  stack  = [(+, 0), (+, 0)]
i = 2
  token = -, len_token = 1
  stack  = [(+, 0), (+, 0)]
  res = 0
  sign = -
i = 3
  token = (, len_token = 1
  stack  = [(-, 0), (+, 0), (+, 0)]
  res = 0
  sign = +
i = 4
  token = 3, len_token = 1
  stack  = [(-, 0), (+, 0), (+, 0)]
  res = 3
  sign = +
i = 5
  token = +, len_token = 1
  stack  = [(-, 0), (+, 0), (+, 0)]
  res = 3
  sign = +
i = 6
  token = 2, len_token = 1
  stack  = [(-, 0), (+, 0), (+, 0)]
  res = 5
  sign = +
i = 6
  token = ), len_token = 1
  stack  = [(+, 0), (+, 0)]
  old_sign, old_res = -, 0
  res = old_res + old_sign.val * res = 0 + (-1) * 5 = -5
  sign = +
i = 7
  token = -, len_token = 1
  stack  = [(+, 0), (+, 0)]
  res = -5
  sign = -
i = 8
  token = (, len_token = 1
  stack  = [(-, -5),(+, 0), (+, 0)]
  res = 0
  sign = +
"""

"""
Basic Calculator II (Medium)
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators 
and empty spaces . The integer division should truncate toward zero.

What if a number is divided by 0???
"""


def calculate(s):
    """
    What if divide by 0?
    "3+2*2" = 7
    "3-2*2" = -1
    "3 - 2 * 2 / 3 + 1" = 2
    """
    s += '+'
    res = 0  # 3
    sign = '+'  # + - * /
    num = 0  # current number
    exp = 1  # value of current group with * and / # -2 * 2 / 3
    for c in s:
        if c in "*/":
            if sign == "+":
                exp = num
            elif sign == "-":
                exp = - num
            elif sign == "*":
                exp = exp * num
            elif sign == "/":
                exp = int(exp / num)
            num = 0
            sign = c
        elif c in "+-":
            if sign == "+":
                res += num
            elif sign == "-":
                res -= num
            elif sign == "*":
                exp = exp * num
                res += exp
            elif sign == "/":
                exp = int(exp / num)
                res += exp
            num = 0
            sign = c
        elif c.isdigit():
            num = num * 10 + int(c)
    return res


"""
Basic Calculator III (Hard)

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . 
The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
"""

from collections import deque


class Solution(object):
    def simple_calculate(self, s_deque):
        """
        What if divide by 0?
        "3+2*2" = 7
        "3-2*2" = -1
        "3 - 2 * 2 / 3 + 1" = 2
        """
        res = 0  # 3
        sign = '+'  # + - * /
        num = 0  # current number
        exp = 1  # value of current group with * and / # -2 * 2 / 3
        while len(s_deque):
            c = s_deque.popleft()
            if c in "*/":
                if sign == "+":
                    exp = num
                elif sign == "-":
                    exp = - num
                elif sign == "*":
                    exp = exp * num
                elif sign == "/":
                    exp = int(exp / num)
                num = 0
                sign = c
            elif c in "+-":
                if sign == "+":
                    res += num
                elif sign == "-":
                    res -= num
                elif sign == "*":
                    exp = exp * num
                    res += exp
                elif sign == "/":
                    exp = int(exp / num)
                    res += exp
                num = 0
                sign = c
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == "(":
                num = self.simple_calculate(s_deque)
            elif c == ")":
                s_deque = deque(["+"])
        return res

    def calculate(self, s):
        s_deque = deque(s)
        s_deque.append('+')
        return self.simple_calculate(s_deque)
