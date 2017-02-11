
/////////////////////////////////////////////////////////////////
///                        README.txt                         ///
/////////////////////////////////////////////////////////////////

Author:  Jason W Gould
Program: Forward Chaining - Tic Tac Toe!

Tested on Python version: 2.7.6

================================================================
===                   FILES REQUIRED TO RUN                  ===
================================================================

1. fc.py        (Python Program)
2. ttt.kb       (Knowledge base) 

================================================================
===                       INSTRUCTIONS:                      ===
================================================================

1.  This program uses forward chaining to suggest the next best possible
    move. It works by applying the forward chaining algorithm and the user
    input board state to the knowledge base I defined in ttt.kb

2.  To use the forward chaining program, simply run 
    fc.py with the knowledge base and board state:

EX STATE:      
    |_O_|___|___| 
    |_O_|___|_X_| 
    |_X_|___|___| 

INPUT:
    > python fc.py ttt.kb "o11 b12 b13 o21 b22 x23 x31 b32 b33 turn_x"

OUTPUT:
    ...
    move_x13_setup

3.  Included files: 
    - Sample program traces and output of example board states:
        trace1.txt, trace2.txt, trace3.txt, trace4.txt
    - Four test states:
        trace5.txt, trace6.txt, trace7.txt, trace8.txt
    - The program:
        fc.py
    - The knowledge base:
        ttt.kb
