from pydoc import plain


def palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return f"{num} is a palindrome"
    return f"{num} is not a palindrome"


number = input("enter the number : ")
check = palindrome(number)
print(check)
