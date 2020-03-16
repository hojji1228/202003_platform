
a = int(input("숫자를 입력하세요: "))

for i in range(a) :
    print(" "*(a-i), '★'*(i+1), " "*(a-i))
for i in range(a) :
    print(" "*(i+2), '★'*(a-i-1), " "*(i+2))