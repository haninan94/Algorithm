N = int(input())

queue = list(range(1, N + 1))
trash = []

while len(queue) > 1:
    trash.append(queue.pop(0))
    queue.append(queue.pop(0))
print(*trash, queue.pop())