n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 시작 시간 순으로 정렬 후 끝 시간으로 정렬
arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])
# 시작 시간 기준점 설정
s, e = 0, arr[0][1]
cnt = 1
for i in arr[1:]:
    # 끝 시간이 다음 시작 시간보다 같거나 그 이전이면
    if e <= i[0]:
        # 시작 시간, 끝 시간 갱신
        s, e = i[0], i[1]
        cnt += 1

print(cnt)