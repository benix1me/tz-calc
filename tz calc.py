def main(input: str):
    user_input2 = input.split()
    if len(user_input2) > 3:
        print("Throws exception")
        exit(0)
    try:
        operation = user_input2[1]
        num1 = int(user_input2[0])
        num2 = int(user_input2[2])
    except:
        print("Throws exception")
        exit(0)
    if num1 < 1 or num2 < 1 or num1 > 10 or num2 > 10:
        print("Throws exception")
        exit(0)
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        print(num1 // num2)
    else:
        print("Throws exception")
        exit(0)
while True:
    main(input())
