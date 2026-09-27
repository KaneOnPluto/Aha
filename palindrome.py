list1=[1,2,3]

copy_list=list1.copy()

copy_list.reverse()

print(copy_list)

if(list1==copy_list):
    print("list element is palindrome")
else:
    print("not palindrome")
