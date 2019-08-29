from collections import defaultdict
from collections import Counter
from collections import deque


class Solution(object):
    def eval(self, expr):
        if type(expr) == deque:
            t = expr.popleft()
            ret_val = None
            if t == "let":
                new_vars = Counter()
                while expr:
                    if len(expr) == 1:
                        ret_val = expr.popleft()
                        ret_val = self.eval(ret_val)
                    else:
                        assign_var = expr.popleft()
                        assign_val = self.eval(expr.popleft())
                        new_vars[assign_var] += 1
                        self.var_val[assign_var].append(assign_val)
                for var, times in new_vars.items():
                    for _ in range(times):
                        self.var_val[var].pop()
                return ret_val
            elif t == "add":
                a = self.eval(expr.popleft())
                b = self.eval(expr.popleft())
                return a + b
            elif t == "mult":
                a = self.eval(expr.popleft())
                b = self.eval(expr.popleft())
                return a * b
        elif type(expr) == int:
            return expr
        else:
            return self.var_val[expr][-1]

    def parse(self, raw_tokens):
        if raw_tokens[0].isdigit():
            return int(raw_tokens)
        elif raw_tokens[0] == '-':
            return -int(raw_tokens[1:])
        elif raw_tokens[0] != "(":
            return raw_tokens

        raw_tokens.popleft()  # "("
        token_list = deque([raw_tokens.popleft()])
        while raw_tokens:
            token = raw_tokens.popleft()
            if token == "(":
                raw_tokens.appendleft(token)
                token_list.append(self.parse(raw_tokens))
            elif token == ")":
                return token_list
            else:
                token_list.append(self.parse(token))
        return token_list

    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        self.var_val = defaultdict(list)  # oldest -> newest
        tokens = expression.replace("(", "( ").replace(")", " )").split(" ")
        syntax_tree = self.parse(deque(tokens))
        return self.eval(syntax_tree)
