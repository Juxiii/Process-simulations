import dodaj_recznie
import wczytaj_plik
import losowo


# MENU ŹRODLA
def menu2(procesy):
    input_good = False
    while not input_good:
        print("1.Dodaj proces recznie | 2.Wczytaj z pliku | 3.Generuj losowo")
        x = int(input())
        if x == 1:
            input_good = True
            dodaj_recznie.dodaj_recznie(procesy)
        elif x == 2:
            input_good = True
            wczytaj_plik.wczytaj_plik(procesy)
        elif x == 3:
            input_good = True
            losowo.generuj(procesy)
