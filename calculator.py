print('Welcome to the greatest calculator of all time')
print('you can quit at any time by typing in:   exit   and pressing enter.')

def calculate():
    a = input("enter your first number:   ")
    if a == 'exit':
        return
    a = float(a)
    while True:
        sign = input('enter a sign : +, -, * or /:  ')
        if sign == 'exit':
            return
        elif sign == '+':
            b = input('enter the second number:   ')
            if b == 'exit':
                return
            b = float(b)
            result = a + b
            print(result)
            break
        elif sign == '-':
            b = input('enter the second number:   ')
            if b == 'exit':
                return
            b = float(b)
            result = a - b
            print(result)
            break
        elif sign == '*':
            b = input('enter the second number:   ')
            if b == 'exit':
                return
            b = float(b)
            result = a * b
            print(result)
            break
        elif sign == '/':
            b = input('enter the second number:   ')
            if b == 'exit':
                return
            b = float(b)
            result = a / b
            print(result)
            break
        else:
            print('This sign does not exist, enter: +,  -,  *  or  /  ')

calculate()