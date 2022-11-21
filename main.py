import time
start_time = time.time()

database = "wordbases/slownik.txt"

keyletter = open("input/input.txt", "r", encoding='windows-1250')
keyletter = keyletter.read(1)

wordbase = open(database, "r", encoding='windows-1250')
for x in wordbase:
    x = x.strip()
    if x.startswith(keyletter):
        print(x)

print(" ")
print("--- s% seconds ---" % (time.time() - start_time))