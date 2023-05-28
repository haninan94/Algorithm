def test(a, b):
    while b != 0:
        a, b = b , a%b
    return a
test_case = int(input())

for _ in range(test_case):

    A, B = map(int, input().split(" "))

    if A > B:
        A, B = B, A

    # 최대공약수 구하기
    
    temp = test(A, B)
    print(int((A * B )/ temp))
