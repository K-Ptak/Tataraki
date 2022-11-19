import time
import re
start_time = time.time()

wordlist = []
reversed_wordlist = []
words_with_inputletter = []
starting_words = []
split_words = []
results = []
inputletter = ''


def reverse_word(word):
    return word[::-1]


def load_wordbase(filename, coding):
    with open(filename, "r", encoding=coding) as file:
        for word in file:
            wordlist.append(word.strip())
            reversed_wordlist.append(reverse_word(word.strip()))

def input_from_file(filename, coding):
    input = open(filename, "r", encoding=coding)
    global inputletter
    inputletter = input.read(1)

def output_to_file(filename, coding):
    output = open(filename, "w", encoding=coding)
    for rows in results:
        for columns in rows:
            print(columns)
            output.write(columns)
            output.write(" ")
        output.write("\n")


def find(list, letter):
    for word in list:
        if word[0] == letter and len(word) > 1:
            print(word)
            words_with_inputletter.append(word)

    #for firstword in words_with_inputletter:
     #   for secondword in words_with_inputletter:
      #      if firstword.find(secondword) and firstword != secondword and len(firstword) > len(secondword):
       #         print(f"{firstword} - {secondword}")
        #        starting_words.append(secondword.replace('\n', ''))
         #       split_words.append(firstword.replace('\n', ''))
           #     print(starting_words)
          #      print(split_words)

    for baseword, firstword, secondword in words_with_inputletter, words_with_inputletter, reversed_wordlist:
        if baseword.startswith(firstword) and baseword.endswith(secondword) and baseword != secondword and baseword != firstword and len(baseword) > len(firstword) and len(baseword) > len(secondword):
            print(f"{baseword} - {firstword} {reverse_word(secondword)}")


load_wordbase("wordbases/slownik.txt", "windows-1250")
input_from_file("input.txt", "windows-1250")
find(wordlist, inputletter)#output_to_file("output.txt", "windows-1250")

print(" ")
print("--- s% seconds ---" % (time.time() - start_time))