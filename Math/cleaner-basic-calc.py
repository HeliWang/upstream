"""
Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces. Each Empty Space will separate a token. The intermediate result can be float number, say 5 / 2 = 2.5. 
"1 + 1" = 2
"6 - 4 / 2 " = 4
"2 * ( 5 + 5 * 2 ) / 3 + ( 6 / 2 + 8 )" = 21
"( 2 + 6 * 3 + 5 - ( 3 * 14 / 7 + 2 ) * 5 ) + 3" = -12

Thinking Process:
(1) Simple Expression like 1 - 2
sign = +
res = 0
When encounter number, res += (sign) number

(2) Expression like 1 - 2 * 3 / 4
sign = -
res = 1
temp = None -> 2
temp_sign = None
When encounter op, 
  if + -:
    sign = op
When encounter number or nested expression,
  Check next op
   if next_op is * or /:
     recover current token into deque
     call calc_mult_div(nested_tokens)
     continue
  res = (+ -) val
"""

from collections import deque


def calc_multi_div(nested_tokens):
    op = "*"
    res = 1
    while nested_tokens:
        token = nested_tokens.popleft()
        if token in ["*", "/"]:
            op = token
        elif type(token) == deque or type(token) == float:
            num = token
            if type(token) == deque:
                num = calc(token)
            if op == "*":
                res *= num
            else:
                res /= num
        else:
            nested_tokens.appendleft(token)
            nested_tokens.appendleft(res)
            return
    nested_tokens.appendleft(res)

def calc(nested_tokens):
    op = "+"
    res = 0
    while nested_tokens:
        token = nested_tokens.popleft()
        next_token = nested_tokens[0] if nested_tokens else None
        # print(token)
        if next_token in ["*", "/"]:
            nested_tokens.appendleft(token)
            calc_multi_div(nested_tokens)
            # print(nested_tokens)
            continue
        if token in ["+", "-"]:
            op = token
        else:
            num = token
            if type(token) == deque:
                num = calc(token)
            if op == "+":
                res += num
            else:
                res -= num
    return res

def tokenize(exp_str):
    tokens = deque()
    while exp_str:
        c = exp_str.popleft()
        if c == '(':
            inner_tokens = tokenize(exp_str)
            tokens.append(inner_tokens)
        elif c == ')':
            return tokens
        elif c in "+-/*":
            tokens.append(c)
        else:
            num = ord(c) - ord('0')
            while exp_str and exp_str[0] in "0123456789":
                num *= 10
                num += ord(exp_str.popleft()) - ord('0')
            tokens.append(float(num))
    return tokens


def exp_eval(exp_str):
    exp_str = exp_str.replace(" ", "")
    nested_tokens = tokenize(deque(exp_str))
    return calc(deque(nested_tokens))


assert exp_eval("( 2 + 6 * 3 + 5 - ( 3 * 14 / 7 + 2 ) * 5 ) + 3") == float(-12)
