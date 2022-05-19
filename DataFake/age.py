from random import randint
from typing import List
from datetime import datetime


class Age:
    def __init__(self) -> None:
        self.__age: int = randint(18, 65)

    def age(self):
        return self.__age

    def birth_date(self):
        self.__month31: List[int] = [1, 3, 5, 7, 8, 10, 12]
        self.__month30: List[int] = [4, 6, 9, 11]
        self.__birth_month: int = randint(1, 12)
        self.__current_month: int = datetime.today().month
        self.__current_year: int = datetime.today().year

        if self.__birth_month in self.__month31:
            self.__day = randint(1, 31)
        elif self.__birth_month in self.__month30:
            self.__day = randint(1, 30)
        else:
            self.__day = randint(1, 28)

        if self.__birth_month > self.__current_month:
            self.__current_year -= 1

        self.__birth_year: int = self.__current_year - self.__age
        self.__birth_date: datetime = datetime(
            self.__birth_year, self.__birth_month, self.__day)

        return self.__birth_date.strftime('%d/%m/%Y')


if __name__ == '__main__':
    a = Age()
    print(a.age())
    print(a.birth_date())
