class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mono_stack = []  # sorted, top is min

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.mono_stack or self.mono_stack[-1] >= x:
            self.mono_stack.append(x)

    def pop(self) -> None:
        v = self.stack.pop()
        if self.mono_stack[-1] == v:
            self.mono_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mono_stack[-1]
