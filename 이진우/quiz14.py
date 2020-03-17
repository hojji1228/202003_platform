

W = input('대소문자를 바꿀 알파벳을 입력해 주세요. :')

# .upper = 대문자로 변환
# .lower = 소문자로 변환

s = W.upper()
b = W.lower()

if s == b:
    print('에러')
else:
    if W == s:
        print('결과 : ',b)
    elif W == b:
        print('결과 : ',s)
