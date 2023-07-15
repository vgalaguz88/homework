import random
import string

lowercase = random.choice(string.ascii_lowercase)
uppercase = random.choice(string.ascii_uppercase)
digit = random.choice(string.digits)
symbol = random.choice(string.punctuation)
base_psw = [lowercase, uppercase, digit, symbol]
all_chars = string.digits + string.ascii_letters + string.punctuation


def get_number():
    text, attempt = '', 3
    while attempt > 0:
        try:
            attempt -= 1
            text = input('Please enter the desired password length: ')
            if int(text) >= 4:
                return int(text)
            else:
                print(f'Password length should be 4 symbols or more, you have {attempt} attempt(s) left')
        except ValueError:
            print(f'You entered "{text}", it`s not a number of 4 symbols or more, you have {attempt} attempt(s) left')
    exit('It was you last chance:)')


def generate_password():
    print('Welcome to the Linux User Password Generator!\n')
    arr_chars = []
    try:
        psw_length = get_number()
        arr_chars.extend(random.sample(base_psw, len(base_psw)))
        for i in range(psw_length - len(base_psw)):
            arr_chars.extend(random.sample(all_chars, 1))
        random.shuffle(arr_chars)
        password = "".join(arr_chars)
        print(f'\nGenerated password: {password}')
    except KeyboardInterrupt:
        print('\nThe password generator is stopped by your wish')


generate_password()
