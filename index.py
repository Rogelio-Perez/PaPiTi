import imp
import random
from pyfiglet import figlet_format


def play():
    bienvenida = figlet_format("PaPiTi", font="larry3d")
    print(bienvenida)
    
    user = input("Elige una opcion: 'pi' para piedra 🪨, 'pa' para papel 🧻, 'ti' para tijera ✂️.\n").lower()

    if user != 'pi' and user != 'pa' and user != 'ti':
        print("Elige una opcion valida. ❌")
        return play()

    if user == 'pi':
        print("\nElegiste piedra 🪨")
    elif user == 'pa':
        print("\nElegiste papel 🧻")
    elif user == 'ti':
        print("\nElegiste tijera ✂️")
    
    computer = random.choice(['pi', 'pa', 'ti'])
    if computer == 'pi':
        print("La computadora eligio piedra 🪨")
    elif computer == 'pa':
        print("La computadora eligio papel 🧻")
    elif computer == 'ti':
        print("La computadora eligio tijera ✂️")
        
    if user == computer:
        return 'Empate! 🤝'

    if gano_el_jugador(user, computer):
        return 'Ganaste! 🎉'

    return 'Perdiste 😔'


def gano_el_jugador(jugador, oponente):
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False

print(play())
