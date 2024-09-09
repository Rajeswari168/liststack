class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [] 
    
    def push(self, element):
        if len(self.stack) == self.size:
            print("Stack is overflow")
        else:
            self.stack.append(element)
    
    def pop(self):
        if not self.stack:
            print("Stack is underflow")
        else:
            print(f"{self.stack.pop()} is deleted")
    
    def peek(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print(f"The top element is: {self.stack[-1]}")
    
    def display(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Elements in stack:")
            for i in range(len(self.stack)-1, -1, -1):
                print(self.stack[i])
obj = Stack(3)
obj.push(10)
obj.push(20)
obj.push(30)
obj.pop()
obj.peek()
obj.display()
