# программа для консольного интерфейса

from guesser import Guesser

g = Guesser('СНЕГ')

print("Добро пожаловать на поле чудес!\nЗагаданное слово:")

print(g.get_opened())
while True:
    symbol = input('\nВведите букву: ').upper()

    if (g.has_char(symbol)):
        print('\nОткройте букву ', symbol, '!', sep='')
        g.open_char(symbol)
    else:
        print('\nБуквы ', symbol, ' нет!', sep='')

    print(g.get_opened())

    if g.is_geussed():
        print('\nВы отгадали загаданное слово "',
              g.get_word(), '"!\nСпасибо за игру!', sep='')
        break