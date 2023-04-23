quarter = 25
dime = 10
nickel = 5
penny = 1

T = int(input())
for test_case in range(T):
    pay = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    if pay >= quarter:
        a = pay // quarter
        pay = pay - ((pay//quarter) * quarter)
    if pay >= dime:
        b = pay // dime
        pay = pay - ((pay//dime) * dime)
    if pay >= nickel:
        c = pay // nickel
        pay = pay - ((pay//nickel)*nickel)
    if pay >= penny:
        d = pay // penny
    print(a, b, c, d)