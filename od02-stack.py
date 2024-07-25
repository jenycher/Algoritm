#работа стеков
class Stack:
    def __init__(self):
        self.items =[]
    def is_empty(self): #путой или нет стек
        return self.items == []

    def push(self, item): # Добавление элемента в стек
        self.items.append(item)

    def pop(self): # удаление верхнего элемента
        return self.items.pop()

    def peek(self): #gолучение верхнего элемента без удаления,
        return self.items[-1]

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())