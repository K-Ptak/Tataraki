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
		echo
		python tataraki.py
		echo "Program zostal uruchomiony pomyslnie"
		xdg-open output/raport.html
		read -p "Wcisnij dowolny przycisk by kontynuowac" stop
		menu
		;;
	"2")
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
		echo
		read -p "Wcisnij dowolny przycisk by kontynuowac" stop
		menu
		;;
	"4")
		clear
		exit
		;;
	*)
		echo "Wprowadzono niepoprawne polecenie"
		echo
		read -p "Wcisnij dowolny przycisk by kontynuowac" stop
		menu
		;;
	esac
}

menu
