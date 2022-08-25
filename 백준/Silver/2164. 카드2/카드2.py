from collections import deque

N = int(input())

queue = deque(range(1, N+1))
trash = []

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue.pop())