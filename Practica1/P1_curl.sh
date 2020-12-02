#!/bin/bash

lista=("lzu4p" "LiveOverflow")

for user in "${lista[@]}"
do
	curl -i "https://api.github.com/users/$user/repos" > "$user curl".txt
done

