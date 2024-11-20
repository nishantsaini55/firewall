
import random
import string
import getpass

class Password:
    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    @staticmethod
    def input_name():
        name = input("Enter your Username : ")
        return name

    @staticmethod
    def input_pass():
        passw = getpass.getpass("Enter your password : ")
        return passw

    def generator(self) -> str:
        char_list = string.ascii_letters + string.digits + string.punctuation
        password = self.password + ''.join(random.choice(char_list) for _ in range(12 - len(self.password)))
        print(f"Your password is generated successfully ")
        return password
    
    def key_generator(self) :
         char_list = string.ascii_letters + string.digits 
         key = random.choice(char_list)
         print(f"Your key to access your password is {key}")
         return key



name = Password.input_name()
passw = Password.input_pass()
obj1 = Password(name, passw)
hashed_password = obj1.generator()
key = obj1.key_generator()

    