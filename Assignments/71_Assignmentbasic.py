'''
get a large list of numbers 
a = [32,43,55,11,2,3,4,5,66,33,66,7,567,89,87,54,32,12,34,567,333,256,242,121],
sort the list and search a user given number in list using binary search technique
'''
a = [32,43,55,11,2,3,4,5,66,33,66,7,567,89,87,54,32,12,34,567,333,256,242,121]
a.sort()

usr = int(input(f"{a} \nEnter  number from list to search : "))
def binarySearch(a,s,e):
    pivot = s+(e-s)//2
    if(a[pivot]==usr):
        return pivot
    if(a[pivot] < usr):
        return binarySearch(a,pivot+1,e)
    else:
        return binarySearch(a,s,pivot-1)

indx = binarySearch(a,0,len(a))
print(f"index : {indx} , value : {a[indx]}")
