import random
import string


class PasswordGenerator:
    def __init__(self, length=8, include_uppercase=True, include_lowercase=True, include_digits=True,
                 include_special_chars=True):
        """
        Parameters
        ----------
        length : int, optional
            The password length
        include_uppercase : bool, optional
            Indicating whether to include uppercase letters in the password
        include_lowercase : bool, optional
            Indicating whether to include lowercase letters in the password
        include_digits : bool, optional
            Indicating whether to include digits in the password
        include_special_chars : bool, optional
            Indicating whether to include special characters in the password
        """
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_digits = include_digits
        self.include_special_chars = include_special_chars

    def generate_password(self):
        """
        Generates password based on provided parameters

        Returns:
        str: Generated password
        """
        included_chars = ''
        password_chars_arr = []
        if True not in [self.include_uppercase, self.include_lowercase, self.include_digits,
                        self.include_special_chars]:
            print('You have excluded all the symbols required for the password generating')
            exit()
        if self.length < 4:
            print('Password length should be 4 symbols or more')
            exit()
        if self.include_lowercase:
            # include characters to included_chars to use them in password generating
            included_chars += string.ascii_lowercase
            # add random character to password_chars_arr to have at least one character of required type
            password_chars_arr.extend(random.choice(string.ascii_lowercase))
        if self.include_uppercase:
            included_chars += string.ascii_uppercase
            password_chars_arr.extend(random.choice(string.ascii_uppercase))
        if self.include_digits:
            included_chars += string.digits
            password_chars_arr.extend(random.choice(string.digits))
        if self.include_special_chars:
            included_chars += string.punctuation
            password_chars_arr.extend(random.choice(string.punctuation))

        # extend password_chars_arr with random characters from included_chars of specified length
        for i in range(self.length - len(password_chars_arr)):
            password_chars_arr.extend(random.sample(included_chars, 1))
        random.shuffle(password_chars_arr)
        password = "".join(password_chars_arr)
        return password
