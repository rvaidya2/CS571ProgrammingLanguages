import re # for tokenizer and output list conversion
from collections import namedtuple #for tokenizer
import sys

inputString = sys.argv[3]
newList = []


#Creating tokeniser for input string
Token = namedtuple('Token', ['type','value']) # Defining tokens to be stored

def lexer(text): #Pass input string from 'for' loop
    NUMBER = r'(?P<INT>\d+)' # Regex for all numbers
    WHITESPACE = r'(?P<WHITESPACE>\s+)' # Regex for whitespaces
    INITIALIZER = r'(?P<INITIALIZER>.)' # Regex for all other characters

    tokenizer = re.compile('|'.join([NUMBER, WHITESPACE, INITIALIZER]))
    seen_error = False
    for m in tokenizer.finditer(text):
        if m.lastgroup != 'WHITESPACE': 
            if m.lastgroup == 'INITIALIZER':
                if not seen_error:
                    yield [m.group(), m.group()]
            else:
                yield [m.lastgroup, m.group()]
                seen_error = False
        else:
            seen_error = False
                

for token in lexer(inputString): #Take input string and find elements
    newList.append(token)

#End of tokenizer 



# val
#   : INT
#   | '{' initializers '}'
#   ;  
def valGrammar(newList, SL1):               
    
    if(newList[0][0] == 'INT'):
        SL1.append(newList[0][1])
        integer = newList[0][1]
        int(integer)
        del newList[0]
        return integer       
    
    elif(newList[0][1] == '{' ):
        SL2 = [] #Create new list (Scoping list) for local access during nested lists
        del newList[0]
        try:
            newList[0][0] == 0
        except Exception:
            print("error: expecting '}' but got 'EOF'") # Error handling for incorrect input
            exit(0)
        initializers(newList, SL2)
        if(newList[0][1] == '}' ):
            SL1.append(SL2)
            del newList[0]
            return SL2
            initializers(newList)  
    

# initializers
#   : initializer ( ',' initializer )* ','? //optional comma after last init
#   | //empty
#   ;   

def initializers(newList, SL2):
    initializer(newList, SL2)
    while (newList[0][0] == ','):
        del newList[0]        
        if(newList[0][0] == ','):
            print("error: expecting '}' but got ','")
            del newList[0]
            exit(0)
            # non-zero status after error
        else:
            initializer(newList, SL2) 


# initializer
#   : '[' INT '] '=' val              //simple designated initializer
#   | '[' INT '...' INT ']' '=' val   //range designated initializer
#   | val                             //positional initializer
#   ;       

def initializer(newList, SL2):
    if(newList[0][0] == '['):
        i = 0
        # Check for simple designators
        if((newList[1][0] == 'INT') and (newList[2][0] == ']') and (newList[3][0] == '=')):
            designator = newList[1][1]
            designator = (int(designator))
            del newList[0:4]
            for i in range (len(SL2), designator):
                SL2.append("0")
            valGrammar(newList, SL2)  

        # Check for nested designators   
        elif((newList[1][0] == 'INT') and (newList[2][0] == '.') and (newList[3][0] == '.') and (newList[4][0] == '.') and (newList[5][0] == 'INT') and (newList[6][0] == ']') and (newList[7][0] == '=')):
            designator1 = newList[1][1]
            designator2 = newList[5][1]
            designator1 = (int(designator1))
            designator2 = (int(designator2))
            del newList[0:8]
            # Delete elements that are not significant and run loop to assign value to designated location
            for i in range (len(SL2), designator1): # Simple designators
                SL2.append("0")
            for i in range (designator2 - designator1): #Ranged designators
                SL2.append(newList[0][1])
            valGrammar(newList, SL2)     

        # Error handling for wrong range input
        elif((newList[1][0] == 'INT') and (newList[2][0] == '.') and (newList[3][0] == '.') and (newList[4][0] == 'INT') and (newList[5][0] == ']') and (newList[6][0] == '=')):
            print("error: expecting ']' but got '.'")
            exit(0)

        # Error handling for wrong designator input
        elif((newList[1][0] == 'INT') and (newList[2][0] == '=')):
            print("error: expecting ']' but got '='")
            exit(0)       
        
    else:
        valGrammar(newList, SL2)  # Recursion according to given grammar
    

def baseCases(newList):
    if (len(newList) == 0): #error handling for empty string/EOF
        return exit(0)
    
    elif (len(newList) > 0): 
        return valGrammar(newList, []) #Start of recursive function
            
    else:
        print("Error")



#Put final output in a list of string elements
outputFinal = baseCases(newList)

if (outputFinal != None):   
    #Convert string elements to int elements if output is correct
    print(eval(re.sub(r"'", "", str(outputFinal))))

else:
    print(1) # non-zero status after error





