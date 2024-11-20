
import random
import string
import getpass

class Password:
    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    @staticmethod
    def input_name():
        name = input("ENTER YOUR NAME: ")
        return name

    @staticmethod
    def input_pass():
        passw = getpass.getpass("ENTER YOUR PASSWORD: ")
        print(f"before hashing: {passw}")
        return passw

    def generator(self) -> str:
        char_list = string.ascii_letters + string.digits + string.punctuation
        password = self.password + ''.join(random.choice(char_list) for _ in range(12 - len(self.password)))
        print(f"after hashing: {password}")
        return password


name = Password.input_name()
passw = Password.input_pass()
obj1 = Password(name, passw)
hashed_password = obj1.generator()

    