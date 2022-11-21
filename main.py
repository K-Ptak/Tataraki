import time
start_time = time.time()


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
    wordbank.append(x)
    if x.startswith(keyletter):
        keywords.append(x)

for x in wordbank:
    reversedWordbank.append(x[::-1])

#----------------------------------------------------------#

print(" ")
print("--- s% seconds ---" % (time.time() - start_time))