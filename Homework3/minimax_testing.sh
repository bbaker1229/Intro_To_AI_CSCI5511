#!/bin/bash
white=0
black=0
value=""
for i in {1..100}
do
	# echo -n $i
	value=$(python3 minimax_vs_random.py | grep wins | awk '{print $1;}')
	if [[ "$value" == "White" ]]
	then
		let white+=1
	else
		let black+=1
	fi
done
echo "black=$black"
echo "white=$white"
