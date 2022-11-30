import time
from os import listdir
from os.path import isfile, join

start_time = time.time()


def reverse(word):
    return word[::-1]


def errorcodes(errorname):
    if errorname == "keyletter":
        print("Podana wartosc nie jest litera")
        exit()
    if errorname == "input":
        print("Nie znaleziono pliku input")
        exit()
    if errorname == "dictionary":
        print("Nie znaleziono pliku slownikowego")
        exit()


# -----odczytanie, pobranie i przetworzenie danych------#
database = "wordbases/test.txt"
wordbank = []  # zawiera wszystkie slowa
reversedWordbank = []  # zawiera wszystkie slowa odwrocone

try:
    read = open(database, "r", encoding='windows-1250')
except:
    errorcodes("dictionary")

for x in read:
    x = x.strip()
    if len(x) > 1:
        wordbank.append(x)

for x in wordbank:
    reversedWordbank.append(reverse(x))

inputfiles = [file for file in listdir("input") if isfile(join("input", file))]
for file in range(len(inputfiles)):


    input = f"input/{inputfiles[file]}.txt"

    try:
        keyletter = open(input, "r", encoding='windows-1250')
        keyletter = keyletter.read(1)
        try:
            keyletter.isalnum()
        except:
            errorcodes("keyletter")
    except:
        errorcodes("input")

    keywords = []  # zawiera same slowa zaczynajace sie na keyletter
    for x in wordbank:
        if x.startswith(keyletter):
                keywords.append(x)

    for x in wordbank:
        reversedWordbank.append(reverse(x))

    # ----------------------------------------------------------#
    for fullword in keywords:
        for firstword in keywords:
            for secondword in reversedWordbank:
                if firstword in fullword and len(fullword) - len(firstword) > 1:
                    tempword = fullword.replace(firstword, '')
                    if secondword in tempword and len(secondword) == len(tempword):
                        outputfile = open(f"output/output{file}.txt", "w")
                        outputfile.write(f"{fullword} - {firstword} {reverse(secondword)}")

print(" ")
print("--- s% seconds ---" % (time.time() - start_time))
