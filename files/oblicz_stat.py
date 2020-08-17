import math


def stat(i, kolejka):
    #                             Obliczanie statystyk
    print("Sumaryczny czas:", i)
    sredni_oczekiwania = 0
    sredni_pracy = 0
    for j in kolejka:
        sredni_oczekiwania += j.czas_oczekiwania
        sredni_pracy += j.czas_przetwarzania
    sredni_oczekiwania = sredni_oczekiwania / len(kolejka)
    sredni_pracy = sredni_pracy / len(kolejka)
    print("Średni czas oczekiwania:", sredni_oczekiwania)
    print("Średni czas przetwarzania:", sredni_pracy)
    suma1 = 0
    suma2 = 0
    for j in kolejka:
        suma1 += (j.czas_oczekiwania - sredni_oczekiwania) ** 2
        suma2 += (j.czas_przetwarzania - sredni_pracy) ** 2
    suma1 = suma1 / (len(kolejka) - 1)
    suma2 = suma2 / (len(kolejka) - 1)
    odchylenie1 = math.sqrt(suma1)
    odchylenie2 = math.sqrt(suma2)
    print("Odchylenie standardowe oczekiwania:", odchylenie1)
    print("Odchylenie standardowe przetwarzania:", odchylenie2)
