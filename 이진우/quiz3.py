
import random

referee = input("주사위를 던지세요!")

p1 = random.randint(1, 6)
p2 = random.randint(1, 6)


if p1 > p2:
    print("p1 의 승리입니다.")
elif p1 < p2:
    print("p2의 승리입니다.")
else:
    print("무승부 입니다.")