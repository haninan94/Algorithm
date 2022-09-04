A, B, C = map(int, input().split())  # A는 고정비용 B는 가변비용 C는 노트북

temp = C - B  # 한대팔며 나오는 금액
if temp > 0:
    print(A // (temp) + 1)
else:
    print(-1)