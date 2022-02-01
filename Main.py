divide = "÷"
multiply = "×"
add = "+"
sub = "-"
num1 = int(input("Enter the first number"))
opreater = input("Enter the Opreation type")
num2 = int(input("Enter the second number"))
if opreater == divide :
    result = num1 / num2
    print(result)
elif opreater == multiply :
    result = num1 * num2
    print(result)
elif opreater == add :
    result = num1 + num2
    print(result)
elif opreater == sub :
    result = num1 - num2
    print(result)
else :
    print("Please write one of these opreater= +, -, ×, ÷.")
