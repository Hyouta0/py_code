side1,side2,side3=input("Enter lenght of sider of triangle").strip().split(" ");
if (int(side1)+int(side2) > int(side3))& (int(side2)+int(side3) > int(side1)) & (int(side1)+int(side3)>int(side2)):
    print("is valid triangle");
else :
    print("is not valid triangle");
