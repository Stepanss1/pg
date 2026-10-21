def je_prvocislo(cislo):
    
    cislo = int(cislo)
    
    if cislo <= 1:
        return False
        
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
            
    return True


def vrat_prvocisla(maximum):
    
    maximum = int(maximum)
    seznam_prvocisel = []
    
    for i in range(1, maximum + 1):
        if je_prvocislo(i):
            seznam_prvocisel.append(i)
            
    return seznam_prvocisel


if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
