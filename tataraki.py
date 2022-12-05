import time
import os
from os import listdir
from os.path import isfile, join, exists

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

def common_item(l1, l2): #returns list of items that are the same
    return list(set(l1) & set(l2))

# -----odczytanie, pobranie i przetworzenie danych------#
database = "wordbases/slownik.txt"
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

    if exists(f"output/output{file}.txt"):
        os.remove(f"output/output{file}.txt")

    input = f"input/{inputfiles[file]}"
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
    buffer = []  # zawiera poprzednie wyniki
    for x in wordbank:
        if x.startswith(keyletter):
            keywords.append(x)

    #-------metoda zlaczania slow bez czasem-------------#
    longest_string = max(wordbank, key=len)
    longest_word = len(longest_string)
    wordsbuffer = []
    firstletterbuffer = []
    secondletterbuffer = []
    for x in keywords:
        for y in reversedWordbank:
            if len(x+y) < longest_word:
                wordsbuffer.append(x+y)
                firstletterbuffer.append(x)
                secondletterbuffer.append(y)

    for x in range(0, len(wordsbuffer)):
        if wordsbuffer[x] in keywords:
            print(f"{wordsbuffer[x]} - {firstletterbuffer[x]} - {secondletterbuffer[x]}")
    #print(common_item(keywords, wordsbuffer))
    #-----------------------------------------------------#
    """
    # ----------------------------------------------------------#
    for fullword in keywords:
        for firstword in keywords:
            for secondword in reversedWordbank:
                if firstword in fullword and len(fullword) - len(firstword) > 1 and len(fullword) != len(firstword):
                    tempword = fullword.replace(firstword, '')
                    if secondword in tempword and len(secondword) == len(tempword):
                        result = f"{fullword} - {firstword} {reverse(secondword)}\n"
                        if result in buffer:
                            continue
                        else:
                            outputfile = open(f"output/output{file}.txt", "a")
                            outputfile.write(f"{fullword} - {firstword} {reverse(secondword)}\n")
                            buffer.append(result)
    """

exec(open("raport.py").read())
print(" ")
print("--- s% seconds ---" % (time.time() - start_time))
