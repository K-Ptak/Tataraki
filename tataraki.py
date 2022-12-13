# -*- coding: utf-8 -*-
import os
from os.path import exists
import sys


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
input = str(sys.argv[1])

file_number = ""
for letters in input:
    if letters.isdigit():
        file_number += letters

try:
    keyletter = open(f"input/{input}", "r")
    keyletter = keyletter.read(1)
    try:
        keyletter.isalnum()
    except:
        errorcodes("keyletter")
except:
    errorcodes("input")

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

if exists(f"output/output{file_number}.txt"):
    os.remove(f"output/output{file_number}.txt")

keywords = []  # zawiera same slowa zaczynajace sie na keyletter
buffer = []  # zawiera poprzednie wyniki
for x in wordbank:
    if x.startswith(keyletter):
        keywords.append(x)

longest_word = len(max(keywords, key=len))

wordsbuffer = open(f'temp_wbuffer.txt', 'w')

for x in keywords:
    for y in reversedWordbank:
        if len(x + y) <= longest_word and x + y in keywords:
            wordsbuffer.write(x + y + " " + x + " " + reverse(y) + "\n")

wordsbuffer.close()

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
outputfile.close()
