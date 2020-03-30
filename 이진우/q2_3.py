class Card():

    def __init__(self):
        self.balance = 0

    def charge(self, money):
        self.balance += money
        print("잔액이 {}원 입니다.".format(self.balance))

    def consume(self, usemoney, place):

        if self.balance >= usemoney:
            if place == "마트":
                self.balance -= usemoney
                print('{}에서 {}원을 사용했습니다.'.format(place, usemoney))

            elif place == "영화관":
                self.balance -= usemoney*0.8
                print('{}에서 {}원을 사용했습니다.'.format(place, usemoney*0.8))

        else: print('잔액이 부족합니다.')

    def print(self):
        print("잔액이 {}원 입니다.".format(self.balance))


card = Card()
card.charge(20000)
card.consume(3000,'마트')
card.consume(10000,'영화관')
card.consume(13000,'마트')
card.print()