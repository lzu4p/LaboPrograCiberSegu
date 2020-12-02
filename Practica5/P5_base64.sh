#!/bin/bash

md5_hash2=`md5sum $1`
md5_hash=$2
base64Function=$3

function imageEncoder {
	base64 $1 > "$1 encoded".txt
}

function imageDecoder {
	base64 --decode $1 > "$1 decoded".png
}

if [[ ${md5_hash2:0:32} == $md5_hash ]]
then
	if [[ "$base64Function" == "encode" ]]
	then
		imageEncoder $1
	elif [[ "$base64Function" == "decode" ]]
	then
		imageDecoder $1
	else
		echo No es una opción
	fi
else
	echo El archivo no coincide con el hash
fi

