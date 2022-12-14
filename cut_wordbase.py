name = input("Podaj nazwe pliku: ")
coile = int(input("Podaj co ktore slowo ma byc wpisane do pliku[int]: "))

input_wordbase = open("wordbases/slownik.txt", "r", encoding='windows-1250')
output_wordbase = open(f'wordbases/{name}.txt', 'w')

lines = input_wordbase.readlines()
for i in range(0, len(lines)):
    if i % coile == 0:
        output_wordbase.write(lines[i])
    else:
        continue

output_wordbase.close()