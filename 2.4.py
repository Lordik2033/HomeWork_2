positions_names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in positions_names:
    i=i.title()
    name = i.rpartition(' ')
    print(f'Привет, {name[-1]}!')