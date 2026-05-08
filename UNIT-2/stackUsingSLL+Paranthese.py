class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Stack:
    def __init__(self):
        self.top = None


    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.is_empty():
            return None  
        popped = self.top.data
        self.top = self.top.next
        return popped


    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

  
    def is_empty(self):
        return self.top is None


def is_balanced(string):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in string:
  
        if char in "({[":
            stack.push(char)

        elif char in ")}]":
            if stack.is_empty():
                return False
            top = stack.pop()
            if pairs[char] != top:
                return False


    return stack.is_empty()


test_strings = [
    "{[()]}", 
    "([)]",   
    "((()))",   
    "{[(])}",  
    "",       
]

for s in test_strings:
    print(f"Input: {s} -> Output: {is_balanced(s)}")