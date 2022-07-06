def DecimalToBinary(decimal):
    if decimal > 1:
        DecimalToBinary(decimal // 2)
    print(decimal % 2, end="")
# this way is more pythonic here we make use of the bin() method in python
# decimal = input("Enter a binary number :")
# binary = bin(int(decimal)).replace("0b", "")
# print("The decimal number is :", binary)


def binarytodecimal(binary):
    try:
        decimal = int(binary, 2)
        print("The decimal value is :", decimal)

    except ValueError as e:
        print("Invalid binary number")
        print("please try a valid binary number")


print("MENU:")
print("1: binary to decimal ")
print("2: decimal to binary ")
print("3: Exit ")
try:
    select = int(input("choose the option : "))
    if select == 1:
        binary = input("enter the binary number : ")
        binarytodecimal(binary)
    elif select == 2:
        decimal = int(input("Enter a decimal number :"))
        DecimalToBinary(decimal)
    elif select == 3:
        exit()
    else:
        print("try again choose properly ")
except ValueError as e:
    print("enter a number")
