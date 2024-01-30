'''
"27","print patterns -- Tejas to fill this","27_Assignmentloops","loops","","","","","","","","","",""
      *
    * *
  * * *
* * * *
'''
n =4
for i in range(n,0,-1):
    for j in range(i-1):
        print(" ",end=" ")
    for k in range(n-i+1):
        print("*",end=" ")
    print()