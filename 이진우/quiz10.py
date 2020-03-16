

def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret
try:
    n = int(input("숫자를 입력하세요. :"))
    print(factorial(n))
except:
    print('예외가 발생했습니다.')