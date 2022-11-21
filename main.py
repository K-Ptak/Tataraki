import time
start_time = time.time()

database = "wordbases/slownik.txt"


wordbase = open(database, "r", encoding='windows-1250')
for x in wordbase:
    print(x.strip())





print(" ")
print("--- s% seconds ---" % (time.time() - start_time))