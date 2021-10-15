Bryan Baker
bake1358@umn.edu
CSCI 5511 - Intro to AI
Homework 3 - Adversarial Search: Othello

Finding my code:
My code should be in a file called: HW3.py.  
This file is a copy of the othellogame.py file that we were given.  I have put my code within two comments marking the beginning of my code and the end of my code.

Testing my code:
I created another python script called: arena.py.
This file imports my code and then runs several different games between different opponents.  
This file can take a while to run fully.  I may have the settings playing 100 games.  Please feel free to adjust the loops to finish in a time better for you.

Utility function:
I created the utility function that counts the difference between a players pieces and their opponent.  
I also played around with a utility_eval function where I returned the number of available moves in that state.  I worked but I couldn't see where that player won anymore games than a player that just used the count difference.

Observations:
Two random players playing against each other have the quickest move time and they win about 50% of the time.
