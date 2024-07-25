#Очередь (Queue) — это структура данных, работающая по принципу "первый пришел — первый ушел" (First In, First Out).

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

print(f'Список пустой= {queue.is_empty()}')

queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

print(f'Список пустой= {queue.is_empty()}')
print(f'Размер списка= {queue.size()}')
print(f'Удалим={queue.dequeue()}') #удалим из очереди'
print(f'Размер списка= {queue.size()}')