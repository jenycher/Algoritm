#Реализовать стек и очередь с помощью списка.
#Дополнительно реализовать другие рассмотренные на уроке структуры.
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

print('Вывод информации о работе стека')
print(f'Стек пустой={stack.is_empty()}')
print('Добавляем 3 значения')
stack.push(4)
stack.push(5)
stack.push(6)

print('Еще раз проверим пустой ли стек')
print(f'Стек пустой={stack.is_empty()}')
print('Удалим верний элемент')
stack.pop()
print(f'Верхний элемент после удаления={stack.peek()}')

print('-' * 30)

#-----------
class Queue:
   def __init__(self):
       self.items = []

   def is_empty(self):
       return self.items == []

   def enqueue(self, item):
       self.items.insert(0, item)

   def dequeue(self):
       return self.items.pop()

   def size(self):
       return len(self.items)

queue = Queue()

print(f'Список очереди пустой= {queue.is_empty()}')

queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

print(f'Список очереди пустой= {queue.is_empty()}')
print(f'Размер списка очереди= {queue.size()}')
print(f'Удалим элемент из очереди={queue.dequeue()}') #удалим из очереди'
print(f'Размер списка после удаления= {queue.size()}')
