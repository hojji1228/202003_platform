a = int(input("첫 번째 숫자를 입력해 주세요: "))
b = int(input("두 번째 숫자를 입력해 주세요: "))

def gcd(a,b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
            (a, b) = (b, a % b)
    return a

print(gcd(a, b))