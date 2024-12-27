import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class RandomAccountProfileData:
    @staticmethod
    def get_email():
        length = random.randint(1, 5)
        email1 = randomword(length)
        length = random.randint(1, 5)
        email2 = randomword(length)
        length = random.randint(1, 3)
        email3 = randomword(length)
        return f"{email1}@{email2}.{email3}"

    @staticmethod
    def get_name():
        length = random.randint(1, 10)
        return randomword(length)

    @staticmethod
    def get_pass():
        length = random.randint(6, 10)
        return randomword(length)