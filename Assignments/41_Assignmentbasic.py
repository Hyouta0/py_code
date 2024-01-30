# write a function to compare two lists, fuction should return 1 if list are same and 0 if list are not same.

def cmp_list(lst1,lst2):
    if(lst1 == lst2):
        return 1;
    return 0;

lst1 =[1,2,3,4,5];
lst2 =[1,2,3,4,5];
lst3 =[1,3,2,4,5];

print(cmp_list(lst1,lst2));
print(cmp_list(lst1,lst3));

