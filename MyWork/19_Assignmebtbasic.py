'''
"19","get marks for a student and print grade (if < 30, fail, <50 third class, <60 second class, <70 first class, >=70 distinction, =100 then gold medal","19_Assignmentconditional statements","conditional statements","","","","","","","","","",""
'''
marks =int(input("Enter your Marks"));
if(marks < 30):
    print("fail");
elif(marks < 50):
    print("third class");
elif(marks < 60):
    print("dinstition");
elif(marks >= 70):
    print("first class");
else:
    print("distintion");
    if(marks == 100):
        print("gold medal");


