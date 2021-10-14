#!/bin/bash

echo "Two Random Players:"
white=0
black=0
value=""
for i in {1..100}
do
	# echo -n $i
	value=$(python3 RandomPlayers.py | grep wins | awk '{print $1;}')
	if [[ "$value" == "White" ]]
	then
		let white+=1
	else
		let black+=1
	fi
done
echo "black=$black"
echo "white=$white"
echo ""

echo "Black = Random; White = Minimax"
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
echo ""

echo "Black = Random; White = Alpha-Beta"
white=0
black=0
value=""
for i in {1..100}
do
	# echo -n $i
	value=$(python3 alphabeta_vs_random.py | grep wins | awk '{print $1;}')
	if [[ "$value" == "White" ]]
	then
		let white+=1
	else
		let black+=1
	fi
done
echo "black=$black"
echo "white=$white"
echo ""
