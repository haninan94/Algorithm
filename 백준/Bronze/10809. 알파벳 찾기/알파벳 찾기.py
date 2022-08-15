s = input()
counts = [-1] * 26
for i in range(len(s)):
    counts[ord(s[i])-97] = s.find(s[i])
print(*counts)