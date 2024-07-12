import random

print("pedra, papel, tesoura, vai!")

pedra = 1
papel = 2
tesoura = 3

jogada_pc = random.randint(1,3)

jogada_pl = input()

## coiso a dizer as jogadas de cada um
if jogada_pc == 1 :
    print("o pc jogou pedra")
if jogada_pc == 2 :
    print("o pc jogou papel")
if jogada_pc == 3 :
    print("o pc jogou tesoura")
print("tu jogaste " + jogada_pl)

## traduzir jogada pessoa para numero
if jogada_pl == "pedra" :
    jogada_pl = 1
elif jogada_pl == "papel" :
    jogada_pl = 2
elif jogada_pl == "tesoura" :
    jogada_pl = 3

## comparar e ver resultado do jogo
if jogada_pc == 1 :
    if jogada_pl == 1 :
        print("Empate :|")
    elif jogada_pl == 2 :
        print("Ganhaste :)")
    elif jogada_pl == 3 :
        print("Perdeste :(")

if jogada_pc == 2 :
    if jogada_pl == 2 :
        print("Empate :|")
    elif jogada_pl == 3 :
        print("Ganhaste :)")
    elif jogada_pl == 1 :
        print("Perdeste :(")

if jogada_pc == 3 :
    if jogada_pl == 3 :
        print("Empate :|")
    elif jogada_pl == 1 :
        print("Ganhaste :)")
    elif jogada_pl == 2 :
        print("Perdeste :(")