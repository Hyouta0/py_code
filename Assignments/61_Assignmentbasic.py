'''
ask user to enter a string and check 
if the string is a palindrom
'''
word = input("enter you string : ").strip()

rev = ""
for i in range(len(word)-1,-1,-1):
    rev=rev+word[i]
if(word == rev):
    print("word is palindrom")
else:
    print("word is not palindrom")
