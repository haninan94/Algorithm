H, M = map(int, input().split())
C = int(input())

h = C//60
m = C%60
if m+M >= 60:
  H += 1
H = (H+h)%24
M = (M+m)%60

print(H, M)