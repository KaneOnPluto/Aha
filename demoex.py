try:
    a=int(input("enter the value of a.."))
    b=int(input("enter the value of b.."))

    c=a/b
    print(c)
except Exception as e:
    print("you can not divide any number with zero..")
    print("Exception is..",e)

else:
    print("in else block")
