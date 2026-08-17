from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()
        self.top_element = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self.top_element = x

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.top_element = self.q.popleft()
            self.q.append(self.top_element)
        return self.q.popleft()

    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()