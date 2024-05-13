import random
continuar = "S"
Perro = 0
Pacerto = 0

while continuar.upper() == "S" :
    ns = random.randint(1,10)
    T = 3
    while(T > 0):
        print("você tem", T, "Tentativa(s)")
        T = T - 1
        nc = int(input("digite um número entre 1 e 10: "))

        if (ns == nc):
            print("você acertou!")
            T = 0
            Pacerto = Pacerto + 1
        else:
            print("você errou.")
            Perro = Perro + 1
        print("número de acertos: ", Pacerto)
        print("número de erros: ", Perro)

    continuar = input("deseja continuar? (S)im")
