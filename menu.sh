#!/bin/bash

menu(){
	clear
	while read -r line
	do
		echo "$line"
	done < resources/menu.txt

	read -n 1  -s wybor;

	case $wybor in
	"1")
		#Uruchom program
		echo
    for file in "input"/*
    do
      file="${file:6}"
      python tataraki.py "$file"
    done
    python raport.py
		echo "Program uruchomiony pomyslnie, otwieram wygenerowany raport"
		xdg-open raport.html > /dev/null &
		echo
		read -p "Wcisnij dowolny przycisk by kontynuowac" stop
		menu
		;;
	"2")
		#Wyswietl informacje
		echo
		while read -r line
	  	do
			echo "$line"
	  	done < resources/info.txt

		echo
		read -p "Wcisnij dowolny przycisk by kontynuowac" stop
		menu
		;;
	"3")
		#Backup
		echo
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
		read -p "Wcisnij dowolny przycisk by kontynuowac" stop
		menu
		;;
	"4")
		#Wyjdz
		clear
		exit
		;;
	*)
		#Niepoprawne polecenie
		echo "Wprowadzono niepoprawne polecenie"
		echo
		read -p "Wcisnij dowolny przycisk by kontynuowac" stop
		menu
		;;
	esac
}

menu
