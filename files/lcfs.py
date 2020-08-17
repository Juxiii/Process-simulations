import menu2
from graphics import *
import grafika
import oblicz_stat


def lcfs(procesy):
    # wybór źródła listy procesów
    menu2.menu2(procesy)

    # otwarcie okna graficznego i definicja kolorów
    win = GraphWin("Gantt", 1650, 750)
    rysowanie = []
    kolory = "red", "cyan", "green", "yellow", "blue", "pink", "purple"

    i = 0  # iteracja czasu
    zmiana_stat = 0  # iterator witrualnego rozpoczecia procesu (nr elementu tablicy ktory juz czeka)
    element = 0  # element kolejki wykonywany przez procesor
    iterator = 0  # licznik iteracji pojedynczego procesu
    procesor_pracuje = False  # zmienna definiująca czy procesor jest zajęty
    czy_koniec = False  # zmienna sprawdzająca czy wszystkie procesy mają status "zakończony"

    kolejka = sorted(procesy, key=lambda proces: int(proces.start))  # sortowanie kolejki po czasie rozpoczecia
    # print([proces.start for proces in kolejka])

    # GLÓWNA PĘTLA - wykonuje się dopóki WSZYSTKIE elementy nie będą miały status "zakończony"
    while not czy_koniec:
        # sprawdzanie ktore procesy z listy juz czekaja
        if zmiana_stat != len(kolejka):   # warunek by indeksy sie zgadzaly
            while kolejka[zmiana_stat].start <= i:
                kolejka[zmiana_stat].status = 1   # zmiana statusu procesu
                zmiana_stat += 1
                if zmiana_stat == len(kolejka):  # sprawdzanie czy wszystkie procesy sa juz dostepne
                    break
        temp = zmiana_stat  # podreczna zmienna (zmienna do sprawdzania jedynie czekających elemntów w jednej z petli)
        if not procesor_pracuje:  # dodawanie procesu do pracy jezeli procesor jest wolny z listy procesow czekajacych
            while temp > 0:  # temp odwrotnie niż w FCFS by zliczać od końca
                if kolejka[temp-1].status == 1 and not procesor_pracuje:  # wybieranie tylko jednego procesu czekającego
                    kolejka[temp-1].status = 2  # ustawienie statusu procesu na "praca"
                    procesor_pracuje = True
                    element = temp-1  # pierwszy znaleziony od końca element będzie wykonywany
                    iterator = kolejka[temp-1].czas  # pobranie czasu procesu procesu do zmiennej
                temp -= 1
        if not procesor_pracuje:  # zabezpieczenie gdyby nie było żadnego procesu po wykonaniu poprzedniej pętli
            i += 1
        while procesor_pracuje:  # obsługa procesu przez procesor dopóki się nie wykona
            if procesor_pracuje:
                if iterator > 0:  # zliczanie procesu
                    iterator -= 1
                    i += 1
                else:  # proces się zakończył
                    procesor_pracuje = False
                    # dane do statystyki
                    kolejka[element].czas_oczekiwania = i - kolejka[element].start - kolejka[element].czas
                    kolejka[element].czas_przetwarzania = kolejka[element].czas_oczekiwania + kolejka[element].czas
                    # zmiana statusu procesu na "ukończony"
                    kolejka[element].status = 3
                    # elementy graficzne
                    rysowanie.append(Rectangle(Point(30 + i - kolejka[element].czas, 20 + 30 * element),
                                               Point(30 + i, 20 + 30 * (element + 1))))
                    rysowanie[-1].setFill(kolory[element % 7])
                    rysowanie[-1].draw(win)
        # sprawdzanie czy wszystkie procesy się zakońćzyły
        czy_koniec = True  # pętla na końcu neguje to wyrażenie gdyby to nie był jeszcze koniec
        for z in kolejka:
            if z.status != 3:
                czy_koniec = False
                break

    oblicz_stat.stat(i, kolejka)  # obliczanie statystyk
    grafika.grafika(win, kolejka, i)  # grafika
