'''
Ask user to enter two strings as command line arguments
and check if 2nd string is subset of 1st string 
without using string functions
'''
import sys

str1 = sys.argv[1]
str2 = sys.argv[2]
flag = False
for i in range(len(str1)):
    if(str1[i] == str2[0]):
        flag = True
        for j in range(1,len(str2)):
            if(str1[i+j] == str2[j]):
                flag = flag and True
            else:
                flag = False

if(flag):
    print("is subset")
else:
    print("is not subset")



