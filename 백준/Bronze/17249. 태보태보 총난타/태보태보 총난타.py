left, right = input().split('0')

left_count = 0
for i in range(len(left)):
  if left[i] == '@':
    left_count += 1
    
right_count = 0
for i in range(len(right)):
  if right[i] == '@':
    right_count += 1

print(left_count, right_count)