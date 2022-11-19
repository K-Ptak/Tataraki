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
		read -p "Wcisnij dowolny przycisk by kontynuowac" stop
		menu
		;;
	"2")
		while read -r line
	  do
		  echo "$line"
	  done < resources/info.txt
		read -p "Wcisnij dowolny przycisk by kontynuowac" stop
		menu
		;;
	"3")
		read -p "Wcisnij dowolny przycisk by kontynuowac" stop
		menu
		;;
	"4")
		clear
		exit
		;;
	*)
		echo "Wprowadzono niepoprawne polecenie"
		read -p "Wcisnij dowolny przycisk by kontynuowac" stop
		menu
		;;
	esac
}

menu
