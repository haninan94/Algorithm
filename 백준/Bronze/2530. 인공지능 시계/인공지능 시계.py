now_time = list(map(int,input().split()))
timer = int(input())
hour = timer//3600
minute = (timer-hour*3600)//60
second = timer%60
# print(hour,minute,second)
# print(now_time)
now_time[2] += second
if now_time[2] >= 60:
    now_time[1] += 1
    now_time[2] -= 60

now_time[1] += minute
if now_time[1] >= 60:
    now_time[0] += now_time[1] // 60
    now_time[1] -= (now_time[1]//60) * 60

now_time[0] += hour
if now_time[0] >= 24:
    now_time[0] = now_time[0] % 24

print(*now_time)