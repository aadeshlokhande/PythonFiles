# ████████████████████ Queue ████████████████████


class Queue:
    def __init__(self):
        self.que = []
    
    def enqueue(self, val):
        self.que.append(val)

    def dequeue(self):
        if len(self.que)>0:
            front = self.que[0]
            self.que = self.que[1:]
            return front
        else:
            return "Queue is empty"

    def display(self):
        print(self.que)

que1 = Queue()
que1.enqueue(10)
que1.enqueue(20)
que1.enqueue(30)
que1.enqueue(40)
print(que1.dequeue())
print(que1.dequeue())
print(que1.dequeue())
print(que1.dequeue())
print(que1.dequeue())

que1.display()



