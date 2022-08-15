word = input()
counts = [0] * 26
for i in range(len(word)):
    if 65 <= ord(word[i]) <= 90:
        temp = ord(word[i])+32
        counts[temp-97] += 1
    else:
        counts[ord(word[i])-97] += 1
max_of_counts = 0

for idx, value in enumerate(counts):
    if value > max_of_counts:
        max_of_counts = value
        max_idx = idx
        
question = 0
for i in range(len(counts)):
    if counts[i] == max_of_counts:
        question += 1
        
    
if question >= 2:
    print('?')
else:
    print(chr(max_idx+65))