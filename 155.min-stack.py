#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []

        

    def push(self, x: int) -> None:
        self.st.append(x)
        

    def pop(self) -> None:
        if len(self.st) > 0:
            del self.st[-1]
        else:
            raise('Stack is empty')
        
        

    def top(self) -> int:
        if len(self.st) > 0:
            return self.st[-1]
        else:
            raise('Stack is empty')        
        

    def getMin(self) -> int:
        if len(self.st) > 0:
            return sorted(self.st)[0]
        else:
            raise('Stack is empty')     

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

