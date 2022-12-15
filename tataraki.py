# -*- coding: utf-8 -*-
import os
import sys
import re

input = str(sys.argv[1])


def reverse(word):
    return word[::-1]


def errorcodes(errorname):
    if errorname == "keyletter":
        sys.exit(f"{input} - Podana wartosc nie jest litera")
    if errorname == "input":
        sys.exit("Nie znaleziono pliku input")
    if errorname == "dictionary":
        sys.exit("Nie znaleziono pliku slownikowego")
    if errorname == "empty":
        sys.exit(f"{input} - Nie znaleziono slowa zaczynajacego sie na ta litere")
    if errorname == "nooutput":
        sys.exit(f"{input} - Nie znaleziono wynikow spelniajacych warunki")


database = "wordbases/slownik.txt"
wordbank = []  # zawiera wszystkie slowa
reversedWordbank = []  # zawiera wszystkie slowa odwrocone

file_number = ""
for letters in input:
    if letters.isdigit():
        file_number += letters

try:
    keyletter = open(f"input/{input}", "r")
    keyletter = keyletter.read(1)
except:
    errorcodes("input")

if not bool(re.match('^[a-zA-Z]*$', keyletter)):
    errorcodes("keyletter")

try:
    read = open(database, "r")
except:
    errorcodes("dictionary")

for x in read:
    x = x.strip()
    if len(x) > 1:
        wordbank.append(x)

read.close()

for x in wordbank:
    reversedWordbank.append(reverse(x))

keywords = []  # zawiera same slowa zaczynajace sie na keyletter
for x in wordbank:
    if x.startswith(keyletter):
        keywords.append(x)

try:
    longest_word = len(max(keywords, key=len))
except:
    errorcodes("empty")

wordsbuffer = open(f'temp_wbuffer.txt', 'w')
buforx=[]
bufory=[]

for x in keywords:
    for y in reversedWordbank:
        if len(x + y) <= longest_word and x + y in keywords:
            if x in buforx and y in bufory:
                pass
            else:
                wordsbuffer.write(x + y + " " + x + " " + reverse(y) + "\n")
                buforx.append(x)
                bufory.append(y)

wordsbuffer.close()

if os.stat("temp_wbuffer.txt").st_size == 0:
    errorcodes("nooutput")

count = 0
with open(r"temp_wbuffer.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass

wordsbuffer_len = count + 1
wordsbuffer = open(f'temp_wbuffer.txt', 'r')
outputfile = open(f"output/output{file_number}.txt", "w")

for x in range(0, wordsbuffer_len):
    line = wordsbuffer.readline().strip()
    word = line.split(" ")[0]
    firstw = line.split(" ")[1]
    secondw = line.split(" ")[2]
    outputfile.write(f"{word} - {firstw} {secondw}\n")

wordsbuffer.close()
os.remove("temp_wbuffer.txt")
outputfile.close()
