#!/bin/bash

stop(){
  echo
	read -p "Wcisnij enter by kontynuowac" enter
	menu
}

menu(){
	clear
	while read -r line
	do
		echo "$line"
	done < resources/menu.txt

	read -n 1  -s wybor;

	case $wybor in
	"1")
	  dir="output"
	  if [ -d $dir ]
		then
			rm -r $dir
		fi
		mkdir $dir
		#Uruchom program
		echo
    for file in "input"/*
    do
      file="${file:6}"
      python tataraki.py "$file"
    done
    if [ -f "temp_wbuffer.txt" ];
		  then
			  rm temp_wbuffer.txt
		fi
    if [ -d $dir ]
    then
	    if [ "$(ls -A $dir)" ]; then
        python raport.py
        echo
		    echo "Program uruchomiony pomyslnie, otwieram wygenerowany raport"
		    xdg-open raport.html </dev/null >/dev/null 2>&1 & disown
		    #not empty
	    else
	      echo "Brak wynikow dzialania programu"
        #empty
	    fi
    fi
	  stop
		;;
	"2")
		#Wyswietl informacje
		echo
		while read -r line
	  	do
			echo "$line"
	  	done < resources/info.txt

		stop
		;;
	"3")
		#Backup
    if [ -f "raport.html" ]; then
      if [ ! -d "backups" ];
		  then
			  mkdir backups
		  fi

		printf -v date '%(%d-%m-%Y-%H:%M:%S)T\n' -1
		mkdir backups/$date

		cp -R input backups/$date
		cp -R output backups/$date
		cp raport.html backups/$date

		echo "Backup został utworzony pomyslnie"
		stop
    else
      echo "Nie znaleziono pliku raport.html"
    fi
		stop
		;;
	"4")
		#Wyjdz
		clear
		exit
		;;
	*)
		#Niepoprawne polecenie
		echo "Wprowadzono niepoprawne polecenie"
		stop
		;;
	esac
}

menu
