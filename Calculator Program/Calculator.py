logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# add function
def add(a, b):
  return a + b

# muttiply function
def  mul(a, b):
    return a * b
# divide function
def div(a , b):
    return a / b

# subtract function
def sub(a, b):
    return a - b

operator = {"+": add,
            "*": mul,
            "/":div,
            "-": sub}
def Calculator():
    print(logo)
    num1 = float(input("What is the first number ?: "))

    for operation in operator:
       print(operation)
    decision = True

    while decision is True:
        operation_symbol = input("Pick an operator from one of these. ")

        num2 = float(input("What is the next number ?: "))
        for operation in operator:
            if operation_symbol == operation:
                res = operator[operation]
        answer = res(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        next_equ = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.:")
        if next_equ is 'y':
            num1 = answer
        else:
             next_equ is 'n'
             decision = False
Calculator()