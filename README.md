# Tataraki i balonik

Projekt stworzony w ramach zaliczenia przedmiotu Języki skryptowe




## Treść zadania

Zadanie pochodzi z olimpiady informatycznej "Algorytmion" Zadanie 3, 2018

W pliku słownik.txt znajduje się słownik, w którym słowa (każde w nowej linii)
posortowane są alfabetycznie.

Napisz program, który dla zadanej początkowej litery słowa, poszukiwał będzie w tym
słowniku wyrazów, które da się podzielić na pewnym miejscu w ten sposób, że zarówno do
miejsca podziału jak i od miejsca podziału (tę część czytamy wspak), tak powstałe słowa
również znajdują się w tym słowniku.

Przykładowo, jeśli podalibyśmy jako argument literę t, to program mógłby znaleźć słowo
tataraki, bo dzieląc je po czwartej literze, otrzymamy słowa tata i ikar, a dla litery b, program
mógłby zwrócić słowo balonik (podział po trzeciej literze na słowa bal i kino).

Zakładamy dodatkowo, że zarówno poszukiwane słowo, jak i jego składowe, są co
najmniej dwuliterowe.

Program ma zwracać wszystkie wyrazy spełniające warunki zadania (na zadaną literę
początkową).

Na potrzeby projektu program przyjmuje i zwraca dane w postaci plików tekstowych, a następnie generuje raport w formie pliku html.


### Przykładowe użycie programu

Input: 
```
a
```

Output: 

![uruchom2](https://user-images.githubusercontent.com/65954097/208218405-adc383f1-896a-43a2-9725-d93331627291.png)


### Uruchomienie programu


```bash
sh menu.sh
```
