  def scrabble_value(word, multipliers = None):
    
    # Initializes a dictionary that holds a key:value pair of a latin alphabet with its point value based on the game Scrabble. 

    d =  {'a':1, 'b':3,
    'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1,
    'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4,
    'w':4, 'x':8, 'y':4, 'z':10}
    
    # Creates two empty lists that stores the amount of times an alphabet has been used.

    t = []
    default = []
   
    # Loops through the entered string (word) parameter.

    for i in range(len(word)):
        default.append(1) 
    
    if multipliers == None:
        multipliers = default
    
    # For-loop Appends the characters to the temporary list, t.

    for ch in word:
        t.append(d[ch.lower()])
        x = multipliers
        result = sum(map(lambda i,j:i*j,t,x))
    return result
