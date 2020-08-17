from projekt import Proces


def wczytaj_plik(procesy):
    file = open("lista_procesow.txt", "r")
    file.readline()
    for i, line in enumerate(file):
        temp = line.split('|', )
        temp[-1] = temp[-1].strip()
        procesy.append(Proces())
        procesy[i].id = int(temp[0])
        procesy[i].start = int(temp[1])
        procesy[i].czas = int(temp[2])
        print(procesy[i].id, procesy[i].start, procesy[i].czas)
