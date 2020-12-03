#!/bin/bash

publicIP=$(curl https://ifconfig.me)
localIP=$(hostname -I)

#echo $publicIP
#echo $localIP

nmap -sV -sC ${localIP:0:12} > nmapIP.txt
nmap -p 80 --script http-jsonp-detection scanme.nmap.org >> nmapIP.txt
nmap -p 12345 --script netbus-brute $publicIP >> nmapIP.txt

base64 < nmapIP.txt > nmapIP_encoded.txt

