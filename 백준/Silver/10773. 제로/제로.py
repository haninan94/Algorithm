import sys

K = int(input())
stack = []
for i in range(1, K+1):
    item = int(sys.stdin.readline())
    if item == 0:
        stack.pop()
    else:
        stack.append(item)
print(sum(stack))
