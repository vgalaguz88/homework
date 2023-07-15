def addition(operand1, operand2):
    return operand1 + operand2


def subtraction(operand1, operand2):
    return operand1 - operand2


def multiplication(operand1, operand2):
    return operand1 * operand2


def division(operand1, operand2):
    try:
        return operand1 / operand2
    except ZeroDivisionError:
        exit('Nice try, division by 0 is impossible (as far as I know...)')


def get_operand(numeral):
    text, attempt = '', 3
    while attempt > 0:
        try:
            attempt -= 1
            text = input(f'Please enter the {numeral} number: ')
            return int(text)
        except ValueError:
            if attempt == 0:
                exit('It was you last chance:)')
            print(f'You entered "{text}", it`s not a number, try again, you have {attempt} attempt(s) left')


operations = {
    '1': 'Addition',
    '2': 'Subtraction',
    '3': 'Multiplication',
    '4': 'Division'
}


def get_operation_options():
    msg = 'Please select an operation:\n'
    for i in range(len(operations)):
        msg += f' {list(operations.keys())[i]}. {operations[str(i + 1)]}\n'
    return msg


def get_operation():
    text, attempt = '', 3
    while attempt > 0:
        attempt -= 1
        print(get_operation_options())
        text = input(f'Enter your choice (1-4): ')
        if attempt == 0 and text not in list(operations.keys()):
            exit('It was you last chance:)')
        elif text not in operations.keys():
            print(f'You entered "{text}", it`s not a number in range {list(operations.keys())}, try again, you have {attempt} attempt(s) left')
        else:
            return operations[text]


def simple_calculator():
    print('Welcome to the Calculator Program!\n')
    try:
        operand1 = get_operand('first')
        operand2 = get_operand('second')
        operation = get_operation()
        result = globals()[operation.lower()](operand1, operand2)
        print(f'\nThe result of {operation.lower()} is: {result}')
    except TypeError:
        print('Try again later')
    except KeyboardInterrupt:
        print('\nThe calculater is stopped by your wish')


simple_calculator()
