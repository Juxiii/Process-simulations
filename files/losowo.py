from projekt import Proces
from random import randint


def generuj(procesy):  # generowanie losowych procesów
    print("Ile procesow?:")
    licznik = int(input())
    for i in range(licznik):
        procesy.append(Proces())
        procesy[i].id = i
        procesy[i].start = randint(1, 400)
        procesy[i].czas = randint(1, 400)
