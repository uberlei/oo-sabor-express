class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):        
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return self._nome

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')
    
    @property
    def ativo(self):
        return 'sim' if self._ativo else 'não'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante = Restaurante('teste 1','Cat Teste 1')
restaurante.alternar_estado()

restaurante = Restaurante('teste 2','Cat Teste 2')

Restaurante.listar_restaurantes()