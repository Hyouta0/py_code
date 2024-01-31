'''
ask user to enter a string, ask user to enter a character,
write a program to check number of occurances of that character
in the string given by user
'''
usrString = input("Enter your string : ")
usrChar = input("Enter character to search : ")
cnt=0
for i in usrString:
    if i == usrChar:
        cnt +=1
print(f"'{usrChar}' has appersed {cnt} times in '{usrString}' .")
