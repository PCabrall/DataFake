from random import randint
from typing import List
import sqlite3


class Name:
    def __init__(self):
        conexao = sqlite3.connect(
            r'C:\DataFake\Data\Names.db')
        cursor = conexao.cursor()

        self.__fullname: List[str] = []

        if randint(1, 2) == 1:
            cursor.execute(
                'SELECT * FROM Female ORDER BY RANDOM() LIMIT 1')
            for linha in cursor.fetchall():
                ident, nome = linha
                nome = nome.split()
                self.__fullname.extend(nome)
        else:
            cursor.execute(
                'SELECT * FROM Male ORDER BY RANDOM() LIMIT 1')
            for linha in cursor.fetchall():
                ident, nome = linha
                nome = nome.split()
                self.__fullname.extend(nome)

        if randint(2, 3) == 2:
            cursor.execute('SELECT * FROM Lastnames ORDER BY RANDOM() LIMIT 2')
            for linha in cursor.fetchall():
                ident, nome = linha
                nome = nome.replace('\n', '')
                self.__fullname.append(nome)
        else:
            cursor.execute(
                'SELECT * FROM Lastnames ORDER BY RANDOM() LIMIT 3')
            for linha in cursor.fetchall():
                ident, nome = linha
                nome = nome.replace('\n', '')
                self.__fullname.append(nome)

        cursor.close()
        conexao.close()

    def __fullname__(self):
        return self.__fullname

    def fullname(self):
        return ' '.join(self.__fullname)

    def name(self):
        return self.__fullname[0]

    def lastname(self):
        if self.__fullname[1].upper() == 'DA' or \
                self.__fullname[1].upper() == 'DE':
            return self.__fullname[2]
        return self.__fullname[1]


if __name__ == '__main__':
    for i in range(1000):
        n = Name()
        print(n.fullname(), ' -> ',
              n.name(), ' |', n.lastname())
