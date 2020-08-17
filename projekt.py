import fcfs
import lcfs
import sjf
import rr


# KLASA PROCESU
class Proces:
    id = 999
    start = 0
    czas = 0
    # status: 0 -> brak | 1 -> czeka | 2 -> pracuje | 3 -> zakonczony
    status = 0
    czas_oczekiwania = 0
    czas_przetwarzania = 0


def main():
    procesy = []
    # MENU GLOWNE
    input_good = False
    x = 1
    while not input_good:
        print("Menu: 1.FCFS 2.LCFS 3.SJF 4.Round-Robin 5. Wyjście")
        x = int(input())
        if x < 1 or x > 5:
            print("Błąd! Jeszcze raz")
        else:
            input_good = True
    if x == 1:
        fcfs.fcfs(procesy)
    if x == 2:
        lcfs.lcfs(procesy)
    if x == 3:
        sjf.sjf(procesy)
    if x == 4:
        rr.rr(procesy)
    if x == 5:
        quit()
    # zapis do pliku
    print("Chcesz zapisać listę procesów? Y/N")
    pytanie = input()
    if pytanie == "Y" or pytanie == "y":
        plik = open("zapisane procesy.txt", "w")
        plik.write("Lp\t\tStart:\t\tCzas:\n")
        for j in procesy:
            plik.write("%d|%d|%d\n" % (j.id, j.start, j.czas))
        plik.close()


if __name__ == "__main__":
    main()
