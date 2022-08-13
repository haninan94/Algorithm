count = 0
original_N = int(input())
N = original_N


def cycle(N):
    global count
    global original_N
    ten_position = N // 10
    one_position = N % 10
    temp = ten_position + one_position
    new_ten_position = one_position * 10
    new_one_position = temp % 10
    new_N = new_ten_position + new_one_position
    count += 1
    if new_N == original_N:
        print(count)
    else:
        cycle(new_N)

cycle(N)