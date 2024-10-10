print("""Bienvenido al juego de papel, piedra o tijera
Gana el mejor de tres
      Instrucciones:
        1. El jugador 1 se registrará 
        2. El jugador 1 elige sus tres tiradas
        3. Se debe ingresar el número de la opción
        4. El jugador 2 se registrará
        5. El jugador 2 elige sus tres tiradas
        6. Se debe ingresar el número de la opción
        7. El ganador se determinará por el mejor de tres o empate
""")
game_rounds = {}
rounds = 3

# Pide el nombre del jugador 1 y sus tiradas
user_1 = input("Nombre jugador 1: ")
key_user_1 = user_1.lower().strip().replace(" ", "") # genera una clave para el diccionario
game_rounds[key_user_1] = {} # crea un diccionario vacío para el jugador 1
print(f"Jugador '{user_1}' elige tus tiradas", end="\n\n")

for i in range(rounds):
    user_1_choice = input(f"Ronda {i + 1} elige:\n1. Piedra, 2. Papel o 3. Tijera? ")
    game_rounds[key_user_1][i] = user_1_choice # guarda la elección del jugador 1 en el diccionario
    
# Pide el nombre del jugador 2 y sus tiradas
print("----------------", end="\n\n")
user_2 = input("Nombre jugador 2: ")
key_user_2 = user_2.lower().strip().replace(" ", "")
game_rounds[key_user_2] = {}
print(f"Jugador '{user_1}'", end="\n\n")
for j in range(rounds):
    user_2_choice = input(f"Ronda {j + 1} elige:\n1. Piedra, 2. Papel o 3. Tijera? ")
    game_rounds[key_user_2][j] = user_2_choice
print("----------------", end="\n\n")


# compara las elecciones de los jugadores
# 1. Piedra
# 2. Papel
# 3. Tijera
points_user_1 = 0
points_user_2 = 0
for k in range(rounds):
    if game_rounds[key_user_1][k] == game_rounds[key_user_2][k]:
        points_user_1 += 1
        points_user_2 += 1
        print(f"Ronda {k + 1}: Empate")
    elif game_rounds[key_user_1][k] == "1" and game_rounds[key_user_2][k] == "3":
        points_user_1 += 1
        print(f"Ronda {k + 1}: {user_1} gana")
    elif game_rounds[key_user_1][k] == "2" and game_rounds[key_user_2][k] == "1":
        points_user_1 += 1
        print(f"Ronda {k + 1}: {user_1} gana")
    elif game_rounds[key_user_1][k] == "3" and game_rounds[key_user_2][k] == "2":
        points_user_1 += 1
        print(f"Ronda {k + 1}: {user_1} gana")
    else:
        points_user_2 += 1
        print(f"Ronda {k + 1}: {user_2} gana")
print("----------------", end="\n\n")

if points_user_1 > points_user_2:
    print(f"El ganador es {user_1}")
elif points_user_1 < points_user_2:
    print(f"El ganador es {user_2}")
else:
    print("Empate")

    
    
# print(game_rounds, end="\n\n")