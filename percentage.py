def perdec(percentage):
    def msg(percentage, rank):
        return f"You have scored : {percentage}% \n You have passed with {rank}"
    if percentage >= 80:
        return msg(percentage, "Distinction")
    elif percentage >= 60 and percentage < 80:
        return msg(percentage, "First division")
    elif percentage >= 50 and percentage < 60:
        return msg(percentage, "Second division")
    elif percentage >= 40 and percentage < 50:
        return msg(percentage, "Third division")
    else:
        return f"You have scored {percentage}% \n Sorry You failed"


per = float(input("enter u r percentage : "))
result = perdec(per)
print(result)
