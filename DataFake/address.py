import sqlite3


class Address:
    def __init__(self):
        while True:
            connection = sqlite3.connect(r'C:\DataFake\Data\Address.db')
            cursor = connection.cursor()
            cursor.execute(
                'SELECT c.city, c.uf, c.ddd, p.cep, p.address, p.bairro \
                    FROM Citys c INNER JOIN Public p WHERE p.id_city = c.id \
                        ORDER BY RANDOM() LIMIT 1')
            for line in cursor.fetchall():
                self.__city, self.__states, self.__ddd, self.__cep, \
                    self.__address, self.__district = line
            cursor.close()
            connection.close()
            if self.__address != '':
                break

    def city(self):
        return self.__city

    def state(self):
        return self.__states

    def street(self):
        return self.__address

    def cep(self):
        return self.__cep

    def district(self):
        return self.__district

    def address(self):
        return f'{self.__address}, {self.__district}, {self.__city}-\
{self.__states}, CEP: {self.__cep}'

    def __ddd__(self):
        return self.__ddd


if __name__ == '__main__':
    while True:
        a = Address()
        print(a.address())
