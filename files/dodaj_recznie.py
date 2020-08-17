from projekt import Proces


def dodaj_recznie(procesy):
    print("Ile procesow?:")
    licznik = int(input())
    for i in range(licznik):
        procesy.append(Proces())
        print("PROCES #", i)
        procesy[i].id = i
        print("Czas rozpoczecia: ")
        procesy[i].start = int(input())
        print("Czas trwania: ")
        procesy[i].czas = int(input())
    for i in procesy:
        print("PROCES: #", i.id)
        print("start:", i.start)
        print("time:", i.czas)
