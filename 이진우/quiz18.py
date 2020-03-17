

file = ['exit.py', 'hi.py', 'playdata.hwp', 'intro.jpg']

new = []

for n in file:
    list = n.split('.')[0]
    new.append(list)

print(new)
