class MinStack:

    def __init__(self):
        #[(当前的值，目前的最小值)]
        self.st = [(0,inf)]


    def push(self, value: int) -> None:
        self.st.append((value,min(value,self.st[-1][1])))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()