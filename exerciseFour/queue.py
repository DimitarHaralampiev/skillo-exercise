queue = []


def is_empty():
    return len(queue) == 0


def enqueue(item):
    queue.append(item)


def dequeue():
    if is_empty():
        return None

    return queue.pop(0)


command = input('Please enter command ')

while command != 'Stop':

    if command == 'Enq':
        item = input('Please enter item ')
        enqueue(item)

    if command == 'Deq':
        deq = dequeue()
        print(deq)

    command = input('Please enter command ')


print(queue)
