#!/bin/bash

function theGame {
	if [[ $a == "69" ]]
	then
		echo Un secreto oscuro
	fi
}

shopt -s lastpipe
echo "$1" | read a
theGame $a
