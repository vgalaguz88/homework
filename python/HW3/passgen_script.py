from password_generator import PasswordGenerator


def get_number():
    """
    Asks the user about the desired password length, gives the user 3 attempts to enter number => 4

    Returns:
        int: Password length
    """
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
    exit('It was you last attempt, cowboy')


def get_bool(symbols_type):
    """
    Asks the user whether he wants to use characters in his password, gives the user 3 attempts to enter (y/n)

    Parameters:
        symbols_type: str
            characters type

    Returns:
        bool: Password length
    """
    text, attempt = '', 3
    while attempt > 0:
        attempt -= 1
        text = input(f'Do you want to have {symbols_type} in your password (y/n): ')
        if text.lower().strip() in ['y', 'ye', 'yes', 'yep']:
            return True
        elif text.lower().strip() in ['n', 'no', 'nope']:
            return False
        elif attempt == 0:
            exit(f'You entered "{text}", it`s not "y" or "n", it was you last attempt')
        else:
            print(f'You entered "{text}", it`s not "y" or "n", try again, you have {attempt} attempt(s) left')


print('Welcome to the Linux User Password Generator!\n')
try:
    pass_length = get_number()
    include_uppercase = get_bool('uppercase letters')
    include_lowercase = get_bool('lowercase letters')
    include_digits = get_bool('digits')
    include_special_chars = get_bool('special chars')
    generator = PasswordGenerator(pass_length, include_uppercase, include_lowercase, include_digits,
                                  include_special_chars)
    print(f'\nGenerated password: {generator.generate_password()}')
except KeyboardInterrupt:
    print('\nThe Password Generator is stopped by your wish')
