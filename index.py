import imp
import random
from pyfiglet import figlet_format


def play():
    bienvenida = figlet_format("PaPiTi", font="larry3d")
    print(bienvenida)
    
    user = input("Elige una opcion: 'pi' para piedra ๐ชจ, 'pa' para papel ๐งป, 'ti' para tijera โ๏ธ.\n").lower()

    if user != 'pi' and user != 'pa' and user != 'ti':
        print("Elige una opcion valida. โ")
        return play()

    if user == 'pi':
        print("\nElegiste piedra ๐ชจ")
    elif user == 'pa':
        print("\nElegiste papel ๐งป")
    elif user == 'ti':
        print("\nElegiste tijera โ๏ธ")
    
    computer = random.choice(['pi', 'pa', 'ti'])
    if computer == 'pi':
        print("La computadora eligio piedra ๐ชจ")
    elif computer == 'pa':
        print("La computadora eligio papel ๐งป")
    elif computer == 'ti':
        print("La computadora eligio tijera โ๏ธ")
        
    if user == computer:
        return 'Empate! ๐ค'

    if gano_el_jugador(user, computer):
        return 'Ganaste! ๐'

    return 'Perdiste ๐'


def gano_el_jugador(jugador, oponente):
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False

print(play())
