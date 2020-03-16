

N = input("구구단을 알아 봅시다 :")

for i in range(9):
    print('{} * {} = {}'.format(N, i+1,int(N)*(i+1)))