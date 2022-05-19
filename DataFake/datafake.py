from age import Age
from CPF import CPF
from contact import Contact


class DataFake(Age, CPF, Contact):
    def __init__(self) -> None:
        Contact.__init__(self)
        Age.__init__(self)
        CPF.__init__(self)

    def datafake(self, dict=False):
        if dict:
            return {
                'nome': self.fullname(),
                'nascimento': self.birth_date(),
                'idade': self.age(),
                'CPF': self.cpf(),
                'telefone': self.phone_number(),
                'email': self.email(),
                'endereco': self.address()
            }

        return f'''
Nome Compelto: {self.fullname()}
Data de Nascimento: {self.birth_date()}
Idade: {self.age()}
CPF: {self.cpf()}
Telefone: {self.phone_number()}
E-mail: {self.email()}
Endereço: {self.address()}
        '''


if __name__ == '__main__':
    for i in range(100):
        df = DataFake()
        print(df.cpf())
