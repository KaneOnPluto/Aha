
# Use of pass statement in Python Program
num = [1, 3, 6, 33, 76, 29, 17, 60, 100, 47, 53, 88]

print('Odd numbers are: ')
for i in num:
    # check if the number is even
    if i % 2 == 0:
        # if even, then pass
        pass
    # print the odd numbers
    else:
        print (i)
