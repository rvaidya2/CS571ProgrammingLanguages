Topic :  This implement a parser for the language specified by the following grammar:
val
  : INT
  | '{' initializers '}'
  ;
 initializers
  : initializer ( ',' initializer )* ','? //optional comma after last init
  | //empty
  ;
initializer
  : '[' INT '] '=' val              //simple designated initializer
  | '[' INT '...' INT ']' '=' val   //range designated initializer
  | val                             //positional initializer
  ;
  
  
 This project has 2 files:
 1. desig-inits.sh 
 2. parser.py

1. desig-init.sh
This file contains contains the script to run the python file on Unix shell. 

2. parser.py
This is the main file. It works on the concept of recursive descent parsing. It executes in a way that the given grammar satisfies the test cases by looping through the functions recursively.

Libraries used:
1. import re --> This library calls regular expressions for two reasons, it is firstly used to check tokenizers for verifying regular expressions and secondly in output to convert the elements of list of datatype string to a datatype of int.
2. import namedtuple --> This library helps in creation of tokens in the lexer function.
3. import sys --> This is required to take input from the user using Unix terminal.

Flow of the project:
The user is required to put a string which is passed into the lexer funtion that creates a list of tokens with parts - type and value. 
According to the type of the token the string is passed to different functions according to the grammar.
The base case checks if the string has length greater than zero and proceeds to recursively parse the functions.

"del" is used to parse through the list to tokens and according to the value and validity of the token, it is either appended or an exception is thrown.
Conditional statements are generally used to check the validity of the tokens.

Functions:
1. valGrammar() --> This corresponds to the val part of the grammar. It checks for INT or { , } and appends accordingly.
2. initializers() --> This corresponds to the initializers part of the grammar. Mainly used to parse and ignore through the commas in the list.
3. initailizer() --> This corresponds to the initializer part of the grammar. Used to check for the designators part of the grammar and assign values accordingly.


References:
1. Stack Overflow
2. GeeksforGeeks
3. https://zdu.binghamton.edu/


Test Cases that work
1. simple INTs
2. empty initializer
3.  simple positional initializers
4.  nested initializer
5.  nested initializer + simple designated initializer + trailing comma 
6.  nested initializer + range designated initializer
  
  
