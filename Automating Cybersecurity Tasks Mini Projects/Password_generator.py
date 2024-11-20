
import logging
import random
import string
import getpass

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('Nanu')

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

        logger.info(f"Password without hashing is: {passw}")
        return passw

    def generator(self) -> str:
        char_list = string.ascii_letters + string.digits + string.punctuation
        password = self.password + ''.join(random.choice(char_list) for _ in range(12 - len(self.password)))  # Assuming a total length of 12 characters
        print(f"after hashing: {password}")
        logger.critical(f"hashed password is: {password}")
        return password


name = Password.input_name()
passw = Password.input_pass()
obj1 = Password(name, passw)
hashed_password = obj1.generator()

    