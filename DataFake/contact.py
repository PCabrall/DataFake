from random import randint, sample, shuffle, choice
from typing import List
from address import Address
from name import Name


class Contact(Address, Name):
    def __init__(self) -> None:
        Address.__init__(self)
        Name.__init__(self)

    def email(self):
        e = sample(self.__fullname__(), 2)
        sym: list = ['_', '-']
        num = ''.join(sample([chr(i) for i in range(48, 58)], 3))
        dominio: list = ['@gmail', '@hotmail', '@outlook', '@yahoo', '@bool']
        term: list = ['.com', '.com.br']
        char = ['', '', choice(sym), num]
        e1 = [e[1]]
        e1.extend(sample(char, 2))
        shuffle(e1)
        self.__e_mail = (e[0] + ''.join(e1) + choice(dominio) +
                         choice(term)).lower().replace(' ', '')
        return self.__e_mail

    def username(self):
        pass

    def password(self):
        self.__lowercase: List[str] = [chr(i) for i in range(97, 123)]
        self.__uppercase: List[str] = [chr(i) for i in range(65, 91)]
        self.__numbers: List[str] = [chr(i) for i in range(48, 58)]
        self.__symbols: List[str] = [chr(i) for i in range(33, 48)]
        self.__chr_password = sample(self.__lowercase, 5) + \
            sample(self.__uppercase, 5) + sample(self.__numbers, 3) + \
            sample(self.__symbols, 3)
        shuffle(self.__chr_password)
        password = ''.join(self.__chr_password)
        return password

    def phone_number(self, formated=True):
        if formated:
            num1: int = randint(7, 9)
            num2: int = randint(100, 999)
            num3: int = randint(1000, 9999)
            return f'+55 ({self.__ddd__()}) 9{num1}{num2}-{num3}'
        return f'+55{self.__ddd__()}9{num1}{num2}{num3}'


if __name__ == '__main__':
    c = Contact()
    for i in range(10):
        print(c.fullname(), ' -> ', c.phone_number())
