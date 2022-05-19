from random import randint


class CPF:
    def cpf(self, formated=True):
        self.__cpf: str = str(randint(100000000, 999999999))
        self.__new_cpf: str = self.__cpf
        self__reverse: int = 10
        self.__total: int = 0
        for i in range(19):
            if i > 8:
                i -= 9
            self.__total += int(self.__new_cpf[i]) * self__reverse
            self__reverse -= 1
            if self__reverse < 2:
                self__reverse = 11
                d = 11 - (self.__total % 11)
                if d > 9:
                    d = 0
                self.__new_cpf += str(d)
                self.__total = 0

        if formated:
            return f'{self.__new_cpf[:3]}.{self.__new_cpf[3:6]}.{self.__new_cpf[6:9]}\
-{self.__new_cpf[9:]}'

        return self.__new_cpf


if __name__ == '__main__':
    c = CPF()
    print(c.cpf(formated=False))
    print(c.cpf())
