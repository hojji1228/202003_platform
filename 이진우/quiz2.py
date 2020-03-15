a = int(input("숫자를 입력해 주세요. : "))
b = input("원하는 연산 기호를 입력해 주세요. (+,-,*,/) : ")
c = int(input("나머지 숫자를 입력해 주세요. : "))

if b == "+":
    result = a + c
elif b == "-":
    result = a - c
elif b == "*":
    result = a * c
elif b == "/":
    result = a / c
else:
    b = input("올바른 연산기호를 입력하세요.")

print("결과는 {} 입니다.".format(result))