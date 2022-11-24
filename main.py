import time
start_time = time.time()
def reverse(x):
    return x[::-1]

#-----odczytanie, pobranie i przetworzenie danych------#
database = "wordbases/slownik.txt"

keyletter = open("input/input.txt", "r", encoding='windows-1250')
keyletter = keyletter.read(1)

read = open(database, "r", encoding='windows-1250')

wordbank = []   #zawiera wszystkie slowa
reversedWordbank = [] #zawiera wszystkie slowa odwrocone
keywords = []   #zawiera same slowa zaczynajace sie na keyletter
for x in read:
    x = x.strip()
    if len(x) > 1:
        wordbank.append(x)
        if x.startswith(keyletter):
            keywords.append(x)

for x in wordbank:
    reversedWordbank.append(reverse(x))

#----------------------------------------------------------#

for fullword in keywords:
    for firstword in keywords:
        for secondword in reversedWordbank:
            if firstword in fullword and len(fullword) - len(firstword) > 1:
                tempword = fullword.replace(firstword, '')
                if secondword in tempword and len(secondword) == len(tempword):
                    print(f"{fullword} - {firstword} {reverse(secondword)}")
print(" ")
print("--- s% seconds ---" % (time.time() - start_time))