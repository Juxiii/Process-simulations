import menu2
from graphics import *
import grafika
import oblicz_stat


def sjf(procesy):
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
    print([proces.start for proces in kolejka])

    # GLÓWNA PĘTLA - wykonuje się dopóki WSZYSTKIE elementy nie będą miały status "zakończony"
    while not czy_koniec:
        if zmiana_stat != len(kolejka):             # warunek by indeksy sie zgadzaly
            while kolejka[zmiana_stat].start <= i:
                kolejka[zmiana_stat].status = 1     # zmiana statusu procesu
                zmiana_stat += 1
                if zmiana_stat == len(kolejka):     # sprawdzanie czy wszystkie procesy sa juz dostepne
                    break
        temp = zmiana_stat  # podreczna zmienna (zmienna do sprawdzania jedynie czekających elemntów w jednej z petli)
        if not procesor_pracuje:  # dodawanie procesu do pracy jezeli procesor jest wolny z listy procesow czekajacych
            najmniejsza_praca = temp - 1  # indeks elementu z najmniejszą pracą do wykonania
            if najmniejsza_praca >= 0:  # sprawdzanie poprawności indeksu
                while temp > 0:  # iteracja po elementach które czekają
                    # porównanie czasu pracy tylko elementów czekających
                    if (kolejka[temp - 1].status == 1 and kolejka[temp - 1].czas <= kolejka[najmniejsza_praca].czas)\
                            or kolejka[najmniejsza_praca].status == 3:
                        najmniejsza_praca = temp - 1
                    temp -= 1
                kolejka[najmniejsza_praca].status = 2  # status "praca" dla wybranego procesu
                procesor_pracuje = True
                element = najmniejsza_praca  # przekazanie indeksu elementu do pracy
                iterator = kolejka[najmniejsza_praca].czas # pobranie czasu procesu procesu do zmiennej
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
