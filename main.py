from functools import reduce
def generadorArchivo(nombrearchivo):

    try:
        file = open(nombrearchivo, "r")
        filepositivos = open("positivos.tsv", "w")
        filenegativos = open("negativos.tsv", "w")
        filenumericos = open("numericos.tsv", "w")
        fileP1 = open("P1.tsv", "w")
        fileB117 = open("B117.tsv", "w")
        fileB1351 = open("B1351.tsv", "w")
        filelogs = open("logs.txt", "w")
        
        lineas = file.readlines()
        positivos = 0
        negativos = 0
        P1 = 0
        B117 = 0
        B1351 = 0

        for linea in lineas:
            string = linea.split("\t")
            lineaNumerico = string[0] + "\t" + string[1] + "\t" + conversionNumerica(string[2])
            filenumericos.write(lineaNumerico + "\n")

            if detectarCepaP1(string[2]):
                fileP1.write(linea)
                filepositivos.write(linea)
                positivos += 1
                P1 += 1
                
            elif detectarCepaB1351(string[2]):
                fileB1351.write(linea)
                filepositivos.write(linea)
                positivos += 1
                B1351 += 1

            elif detectarCepaB117(string[2]):
                fileB117.write(linea)
                filepositivos.write(linea)
                positivos += 1
                B117 += 1            

            else:
                filenegativos.write(linea)
                negativos += 1

        filelogs.write(str(len(lineas)) + "\n")
        filelogs.write(str(positivos) + "\n")
        filelogs.write(str(B117) + "\n")
        filelogs.write(str(B1351) + "\n")
        filelogs.write(str(P1) + "\n")
        
        file.close()
        filepositivos.close()
        filenegativos.close()
        filenumericos.close()
        fileP1.close()
        fileB117.close()
        fileB1351.close()
        filelogs.close()

    except OSError:
        print("El archivo no existe.")

def conversionNumerica(string):

    newString = ""

    for letra in string:

        if letra == "A":
            newString += "1"
        elif letra == "T":
            newString += "2"
        elif letra == "C":
            newString += "3"
        elif letra == "G":
            newString += "4"

    return newString

def detectarCepaB117(string):

    lista = list(string)
    listaA = list(filter(lambda x: x == "A", lista))
    listaT = list(filter(lambda x: x == "T", lista))

    return True if len(listaT)/len(listaA) > 1 else False


def detectarCepaB1351(string):

    stringNumerico = conversionNumerica(string)
    lista = list(stringNumerico)
    listaPares = list(filter(lambda x: int(x) % 2 == 0, lista))
    listaImpar = list(filter(lambda x: int(x) % 2 != 0, lista))
    sumaPares = reduce((lambda x, y: int(x) + int(y)), listaPares)
    sumaImpar = reduce((lambda x, y: int(x) + int(y)), listaImpar)

    return True if sumaPares > sumaImpar else False

def detectarCepaP1(string):

    stringNumerico = conversionNumerica(string)
    stringInverso = stringNumerico[::-1]
    listaNumerica = list(stringNumerico)
    listaInversa = list(stringInverso)
    listaDiagonal = list(map(lambda x, y: int(x) * int(y), stringNumerico, stringInverso))
    suma = reduce((lambda x, y: x + y), listaDiagonal)
    return True if suma > 525 else False

generadorArchivo("examenes.tsv")