class Multi_card():
    def __init__(self):
        self.balance = 0
        print('카드가 발급되었습니다.')


    def charge(self, money):

        self.balance += money
        print('{}원이 충전되었습니다.'.format(self.balance))

    def consume(self, usemoney, place):

        if self.balance >= usemoney:
            if place == "마트":
                self.balance -= usemoney * 0.9
                print('{}에서 {}원을 사용했습니다.'.format(place, usemoney*0.9))

            elif place == "영화관":
                self.balance -= usemoney * 0.8
                print('{}에서 {}원을 사용했습니다.'.format(place, usemoney*0.8))

            elif place == "교통":
                self.balance -= usemoney * 0.9
                print('{}에서 {}원을 사용했습니다.'.format(place, usemoney*0.9))

        else: print('잔액이 부족합니다.')

    def print(self):
        print("잔액이 {}원 입니다.".format(self.balance))



multi_card = Multi_card()
multi_card.charge(20000)
multi_card.consume(5000, '마트')
multi_card.consume(10000, '영화관')
multi_card.consume(2000, '교통')
multi_card.print()