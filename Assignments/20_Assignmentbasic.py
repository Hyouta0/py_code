

symbol = input("Enter th character");
if(symbol.isnumeric()):
    print("the symbol is number")
else:
    symbol = symbol.lower();
    if( symbol in ['a','i','e','o','u']):
        print("symbo is vovel");
    else:
        print("is concenent");
