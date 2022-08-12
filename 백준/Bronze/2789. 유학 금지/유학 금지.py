word = input()
university = 'CAMBRIDGE'

for i in range(len(word)):
  if word[i] in university:
    word = word.replace(f"{word[i]}", "?")
word = word.replace("?", "")
print(word)