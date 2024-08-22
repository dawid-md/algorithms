def is_balanced(input_str):
    obj = Stack()
    for letter in input_str:
        if letter == "(":
            obj.push(letter)
        elif letter == ")":
            if obj.pop() is None:
                return False
    return obj.peek() is None


# don't modify below this line


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]