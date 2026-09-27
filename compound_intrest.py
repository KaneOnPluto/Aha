principal=int(input("enter principal ammount.."))
rate=int(input("enter rate.."))
time=int(input("Enter time.."))
Amount = principal * (pow((1 + rate / 100), time))
print("ammount is..",Amount)
CI = Amount - principal
print("Compound interest is", CI)
