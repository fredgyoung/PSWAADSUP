

class Stack:

    def __init__(self):
        self.alist = []

    def push(self, obj):
        self.alist.append(obj)

    def pop(self):
        return self.alist.pop()

    def peek(self):
        if len(self.alist) > 0:
            return self.alist[-1]


if __name__ == '__main__':

    mystack = Stack()
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    print(mystack.peek())
    print(mystack.pop())
    print(mystack.peek())

