import menu2
from graphics import *
import grafika
import oblicz_stat


def rr(procesy):
    # wybór źródła listy procesów
    menu2.menu2(procesy)

    # wprowadzenie kwantu czasu przez użytkownika
    print("Kwant czasu:")
    kwant = int(input())
    kwant_roboczy = kwant

    # otwarcie okna graficznego i definicja kolorów
    win = GraphWin("Gantt", 1650, 750)
    rysowanie = []
    kolory = "red", "cyan", "green", "yellow", "blue", "pink", "purple"

    i = 0  # iteracja czasu
    zmiana_stat = 0  # iterator witrualnego rozpoczecia procesu (nr elementu tablicy ktory juz czeka)
    element = 0  # element kolejki wykonywany przez procesor
    iterator = []  # licznik iteracji pojedynczego procesu
    procesor_pracuje = False  # zmienna definiująca czy procesor jest zajęty
    czy_koniec = False  # zmienna sprawdzająca czy wszystkie procesy mają status "zakończony"

    kolejka = sorted(procesy, key=lambda proces: int(proces.start))  # sortowanie kolejki po czasie rozpoczecia
    # print([proces.start for proces in kolejka])

    # GLÓWNA PĘTLA - wykonuje się dopóki WSZYSTKIE elementy nie będą miały status "zakończony"
    while not czy_koniec:
        if zmiana_stat != len(kolejka):             # warunek by indeksy sie zgadzaly
            while kolejka[zmiana_stat].start <= i:
                kolejka[zmiana_stat].status = 1     # zmiana statusu procesu
                zmiana_stat += 1
                # dodanie miejsca w liście "iterator" do zapamiętania pozostałego czasu procesu do pracy
                iterator.append(kolejka[zmiana_stat - 1].czas)
                if zmiana_stat == len(kolejka):     # sprawdzanie czy wszystkie procesy sa juz dostepne
                    break
        # dodawanie procesu do pracy jezeli procesor jest wolny z listy procesow czekajacych
        if not procesor_pracuje and zmiana_stat != 0:
            while not procesor_pracuje:
                if element == zmiana_stat:          # odnawianie pętli procesowej
                    element = 0
                if kolejka[element].status != 1:    # jezeli element nie czeka, to sprawdź następny
                    element += 1
                else:                               # jeżeli element spełnia wymagania to ustaw status na "praca"
                    kolejka[element].status = 2
                    procesor_pracuje = True
        if not procesor_pracuje:  # zabezpieczenie gdyby nie było żadnego procesu po wykonaniu poprzedniej pętli
            i += 1
        else:
            while kwant_roboczy > 0 and procesor_pracuje:  # wykonuj kwant razy lub do skończenia procesu
                if procesor_pracuje:
                    if iterator[element] > 1:  # sprawdza czy została praca do wykonania dla procesu
                        iterator[element] -= 1  # zmniejsz pozostały czas pracy
                        kolejka[element].status = 1  # ustawianie na przyszłość statusu procesu na "czeka"
                        kwant_roboczy -= 1
                        i += 1
                    else:  # proces się zakończył
                        # dane do statystyki
                        kolejka[element].czas_oczekiwania = i - kolejka[element].start - kolejka[element].czas
                        kolejka[element].czas_przetwarzania = kolejka[element].czas_oczekiwania + kolejka[element].czas
                        kolejka[element].status = 3
                        i += 1
                        break
            # elementy graficzne
            rysowanie.append(Rectangle(Point(30 + i - kwant + kwant_roboczy, 20 + 30 * element),
                                       Point(30 + i, 20 + 30 * (element + 1))))
            rysowanie[-1].setFill(kolory[element % 7])
            rysowanie[-1].draw(win)

            kwant_roboczy = kwant  # ustawianie kwantu na domyślną wartość
            czy_koniec = True      # pętla na końcu neguje to wyrażenie gdyby to nie był jeszcze koniec
            procesor_pracuje = False
            element += 1           # następny element
        # sprawdzanie czy wszystkie procesy się zakońćzyły
        for z in kolejka:
            if z.status != 3:
                czy_koniec = False
                break

    oblicz_stat.stat(i, kolejka)  # obliczanie statystyk
    grafika.grafika(win, kolejka, i)  # grafika
