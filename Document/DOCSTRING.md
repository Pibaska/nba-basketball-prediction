# Padr�o Docstring
Uma docstring é uma string literal presente na primeira linha da definição de um módulo, classe ou função. O docstring de qualquer objeto pode ser acessado através de um atributo especial chamado `__doc__` .

![Alt Text](https://media.giphy.com/media/PiQejEf31116URju4V/source.gif)

## Sumario
- Classes
- Funç�es

###Classes
```
class qualquerClasse():
"""
    Descricao da classe(Resumo de qual sua funç�o, seus atributos, seus met�dos)   
"""

def __init__(self, algo: int): # Construtor
"""
    Descriç�o do construtor

    Input:
    > algo: descriç�o do atributo

    Output:
    > self.algo: descriç�o do atributo
"""
    self.algo = algo


def metodo(self, algo):
"""
    Descriç�o do met�do

    Input:
    > algo: descriç�o do atributo e seu tipo
    --------
    ex:
    algo: um numero qualquer -> int

    Output:
    > soma: descriç�o do atributo e seu tipo
    -------
    ex:
    soma: a soma de <algo> com <algo> -> int
    
    OBS: colocar '< >' caso mencionar uma variavel no docstring
"""

    soma = algo + algo
    return soma

```

### Funç�es
```
def funcao(self, algo):
"""
    Descriç�o do met�do

    Input:
    > algo: descriç�o do atributo e seu tipo
    --------
    ex:
    algo: um numero qualquer -> int

    Output:
    > sub: descriç�o do atributo e seu tipo
    -------
    ex:
    sub: a substraç�o de <algo> com <algo> -> int

    OBS: colocar '< >' caso mencionar uma variavel no docstring
"""

    sub = algo - algo
    return sub
```