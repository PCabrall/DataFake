# DataFake (Gerador de Dados Validados de Pessoas Fakes)(README em Construção)


Biblioteca desenvolvida com o intuito de facilitar testes que utilizam de dados de pessoas 
reais para serem executados. Como a introdução ja diz, o framework gera uma pessoa real ou
dados separados, como: Nome Completo, Idade, Data de Nascimento, CPF, Endereço e Telefone...

## Funções

### datafake( ):
A função datafake() deriva de todas as funções presentes nessa biblioteca. Ela rotorna todos
os elementos de uma pessoa real.

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
### datafake(dict=True):

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

#### fullname( ):
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
