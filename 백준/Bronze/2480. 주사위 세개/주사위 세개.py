a, b, c = map(int, input().split())

dices = [a, b, c]
max = 0
for dice in dices:
    if dice > max:
        max = dice

if a == b == c:
    print(10000+a*1000)
elif (a == b != c):
    print(1000+a*100)
elif (a==c!=b):
    print(1000+a*100)
elif (a!=b==c):
    print(1000+b*100)
elif (a!=b!=c):
    print(max*100)
 
    
    