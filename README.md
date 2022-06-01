# DataFake (Gerador de Dados Validados de Pessoas Fakes)


Biblioteca desenvolvida com o intuito de facilitar testes que utilizam de dados de pessoas 
reais para serem executados. Como a introdução ja diz, o framework gera uma pessoa real ou
dados separados, como: Nome Completo, Idade, Data de Nascimento, CPF, Endereço e Telefone...

## Funções

### datafake( ):
A função datafake() deriva de todas as funções presentes nessa biblioteca. Ela rotorna todos os elementos de uma pessoa real. Na função existe um parâmetro datafake(dict=True) que vem como padrão False, retorna um dicionário com todos os valores.

```python
from DataFake import datafake

pessoa = datafake()
print(pessoa)
```
Output:
```
Nome Compelto: Ana Beatriz Hidelfonso Faria Lutz
Data de Nascimento: 28/01/1962
Idade: 60
CPF: 716.931.838-54
Telefone: +55 (84) 97454-3087
E-mail: _hidelfonsolutz@outlook.com.br
Endereço: Rua Antônio Balbino 117, Centro, Triunfo Potiguar-RN, CEP: 59685970
```

Com a função datafake(dict=True) gera um dicionário com: nome, nascimento, idade, CPF, telefone, email e endereco.

```python
from DataFake import datafake

pessoa = datafake(dict=True)
print(pessoa)
```
Output:
```
{'nome': 'Ana Beatriz Hidelfonso Faria Lutz', 'nascimento': '28/01/1962', 'idade': 60,
'CPF': '716.931.838-54', 'telefone': '+55 (84) 97454-3087', 'email': '_hidelfonsolutz@outlook.com.br', 
'endereco': 'Rua Antônio Balbino 117, Centro, Triunfo Potiguar-RN, CEP: 59685970'}
```

### fullname( ):
A função fullname() retorna um Nome Completo de uma pessoa, contendo nomes e
sobrenomes reais.

```python
from DataFake import fullname

nome_completo = fullname()
print(nome_completo)
```
Output:
```
Alice Victória de Deus Bandeira
```
### name( ):
Diferente, porém herdeira da função fullname(), a função name() retorna apenas um único nome ao invés dele compelto,
retornando assim apenas o primeiro nome.

```python
from DataFake import name

nome = name()
print(nome)
```
Output:
```
Alice
```
### lastname( ):
Muito similar a função name(), de retornar apenas um único nome, a função lastname() retorna apenas um sobrenome.

```python
from DataFake import lastname

sobrenome = name()
print(sobrenome)
```
Output:
```
Victória
```
### email( ):
A função email() gerar um e-mail baseado no nome do cidadão.

```python
from DataFake import email

email = email()
print(email)
```
Output:
```
victoriaalice@gmail.com
```
### username( ):
Parecido com todas as outras funções, a função username() retorna um nome de usuário.

```python
from DataFake import username

username = username()
print(username)
```
Output:
```
victoriaalice
```
### password( ):
A função password() retorna uma senha forte com 16 digitos contendo: Numéros, Letras Maiúsculas, Letras Minúsculas e Símbolos.

```python
from DataFake import password

password = password()
print(password)
```
Output:
```
nK.0ZUCEb+7%xr4t
```
### phone_number( ):
A função phone_number() gera um número baseado no estado do cidadão, no formato: +55 (DDD) 9 Digitos.

```python
from DataFake import phone_number

phone_number = phone_number()
print(phone_number)
```
Output:
```
+55 (11) 97807-1611
```
### cpf():
Como a própria função já diz, a função cpf() gera um cpf válido. A função também trás uma parametro de formatação, cpf(formated=True) que por definição é Verdadeiro gerando um CPF formatado como mostra abaixo.

```python
from DataFake import phone_number

cpf = cpf()
print(cpf)
```
Output:
```
733.099.563-00
```

Com o parâmetro formated=False ele remove a formatação do CPF como mostra abaixo.

```python
from DataFake import phone_number

cpf = cpf(formated=False)
print(cpf)
```
Output:
```
73309956300
```
