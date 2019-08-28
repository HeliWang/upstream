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
  if * /:
    temp_sign = op
When encounter number, 
  Check next op
  if * / and temp == None:
    temp = number
  elif * / and temp != None:
    temp (temp_sign)= number
  elif + - and temp != None:
    temp (temp_sign)= number
    res += (sign) temp
    temp = None
    temp_sign = None
    sign = + or -
  elif already end at expression and temp != None:
     temp (temp_sign)= number
     res += (sign) temp
     temp = None
     temp_sign = None
  else:
    res += (sign) number
return res
10 mins for the block


(2) Expression like 2 * ( 5 + 5 * 2 ) / 3 + ( 6 / 2 + 8 ) 
First Translate Bracket Into Nested Expression
sign = -
res = 1
temp = None -> 2
temp_sign = None
When encounter op, 
  if + -:
    sign = op
  if * /:
    temp_sign = op
When encounter number or Nested Exp (like a value), 
  Check next op
  if next op is in [* /]:
   if temp == None:
    temp = number
    if temp != None:
     temp (temp_sign)= number
  elif + - and temp != None:
    temp (temp_sign)= number
    res += (sign) temp
    temp = None
    temp_sign = None
  elif already end at expression and temp != None:
     temp (temp_sign)= number
     res += (sign) temp
     temp = None
     temp_sign = None
  else:
    res += (sign) number
return res
10 mins for the block
"""


def calc(nested_tokens):
    op = "+"
    res = 0
    temp = None
    temp_op = None
    for i, token in enumerate(nested_tokens):
        next_token = nested_tokens[i + 1] if i < len(nested_tokens) - 1 else None
        if token in ["+", "-"]:
            op = token
        elif token in ["*", "/"]:
            temp_op = token
        else:
            num = token
            if type(token) == list:
                num = calc(token)
            if next_token in ["*", "/"]:
                if temp is None:
                    temp = num
                elif temp_op == "*":
                    temp *= num
                elif temp_op == "/":
                    temp /= num
            else:
                if temp is not None:
                    if temp_op == "*":
                        temp *= num
                    elif temp_op == "/":
                        temp /= num
                    if op == "+":
                        res += temp
                    else:
                        res -= temp
                    temp = None
                    temp_op = None
                elif op == "+":
                    res += num
                else:
                    res -= num
    return res


print(calc([30, "+", 22, "-", 50]))
print(calc([30, "+", 22, "-", 5]))
print(calc([30, "+", 22, "/", 5]))
print(calc([30, "+", 22, "/", 5, "*", 10]))
print(calc([30, "+", 22, "/", 5, "*", 10, "+", [[10, "*", 20], "-", 5, "*", 6]]))
# 30 + 22 / 5 * 10 + ((10*20) - 5 * 6)
# 30 + 44 + 170
# Already 31 mins!

import collections


def tokenize(exp_str):
    tokens = []
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
            tokens.append(num)
    return tokens


print(tokenize(collections.deque("( 2 + 6 * 3 + 5 - ( 3 * 14 / 7 + 2 ) * 5 ) + 3".replace(" ", ""))))


# "( 2 + 6 * 3 + 5 - ( 3 * 14 / 7 + 2 ) * 5 ) + 3"
def exp_eval(exp_str):
    exp_str = exp_str.replace(" ", "")
    nested_tokens = tokenize(collections.deque(exp_str))
    return calc(nested_tokens)


print(exp_eval("( 2 + 6 * 3 + 5 - ( 3 * 14 / 7 + 2 ) * 5 ) + 3"))
# - 12
# Spend 51 mins
