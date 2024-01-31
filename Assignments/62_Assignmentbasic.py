'''
Ask user to enter 2 lists of 5 elements each 
(user should enter as comma separated string), 
generate lists from the strings and check if 
two lists entered by user are same
'''
usrList1=input("Enter your first list : ").strip().split(",")
usrList2=input("Enter your second list : ").strip().split(",")
if(usrList1 == usrList2):
    print("Lists are same ")
else:
    print("lists are different")
