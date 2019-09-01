class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0

        nums, ops = [], []
        len_s = len(s)
        i = 0
        while i < len_s:
            if s[i].isdigit():
                num = s[i]
                while i + 1 < len_s and s[i + 1].isdigit():
                    i += 1
                    num += s[i]
                nums.append(int(num))
            elif s[i] == '(':
                ops.append(s[i])
            elif s[i] == ')':
                while ops[-1] != '(':
                    self.calculation(ops, nums)
                ops.pop()
            elif s[i] in '+-*/':
                if ops and self.precedence(ops[-1], s[i]):
                    self.calculation(ops, nums)
                ops.append(s[i])
            i += 1

        while ops:
            self.calculation(ops, nums)

        return nums.pop()

    def calculation(self, ops, nums):
        sign, n2, n1 = ops.pop(), nums.pop(), nums.pop()
        nums.append(self.operation(sign, n1, n2))
        return

    def operation(self, sign, n1, n2):
        if sign == '+':
            return n1 + n2
        elif sign == '-':
            return n1 - n2
        elif sign == '*':
            return n1 * n2
        elif sign == '/':
            return n1 // n2

    def precedence(self, prev_op, curr_op):
        if prev_op in '(':
            return False
        if prev_op in '+-' and curr_op in '*/':
            return False
        return True
