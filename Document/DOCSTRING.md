# Padrao Docstring
Uma docstring é uma string literal presente na primeira linha da definição de um módulo, classe ou função. O docstring de qualquer objeto pode ser acessado através de um atributo especial chamado `__doc__` .

![Alt Text](https://media.giphy.com/media/PiQejEf31116URju4V/source.gif)

## Sumario
- Classes
- Funçoes

### Classes
```
class qualquerClasse():
"""
    Descricao da classe(Resumo de qual sua funçao, seus atributos, seus metodos)   
"""

def __init__(self, algo: int): # Construtor
"""
    Descriçao do construtor

    Input:
    > algo: descriçao do atributo

    Output:
    > self.algo: descriçao do atributo
"""
    self.algo = algo


def metodo(self, algo):
"""
    Descriçao do metado

    Input:
    > algo: descriçao do atributo e seu tipo
    --------
    ex:
    algo: um numero qualquer -> int

    Output:
    > soma: descriçao do atributo e seu tipo
    -------
    ex:
    soma: a soma de <algo> com <algo> -> int
    
    OBS: colocar '< >' caso mencionar uma variavel no docstring
"""

    soma = algo + algo
    return soma

```

### Funçoes
```
def funcao(self, algo):
"""
    Descriçao do metodo

    Input:
    > algo: descriçao do atributo e seu tipo
    --------
    ex:
    algo: um numero qualquer -> int

    Output:
    > sub: descriçao do atributo e seu tipo
    -------
    ex:
    sub: a substraçao de <algo> com <algo> -> int

    OBS: colocar '< >' caso mencionar uma variavel no docstring
"""

    sub = algo - algo
    return sub
```