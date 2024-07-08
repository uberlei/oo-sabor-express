from modelos.avaliacao import Avaliacao

class Restaurante:
    """Representa um restaurante e suas características."""

    restaurantes = []

    def __init__(self, nome, categoria):        
        """
        Inicializa uma instância de Restaurante.
        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
                 
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return self._nome

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}')
    
    @property
    def ativo(self):
        return 'sim' if self._ativo else 'não'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self,cliente, nota):        
        if 0 < nota <= 5 :        
            avaliacao = Avaliacao(cliente,nota)
            self._avaliacao.append(avaliacao)
            
    @property        
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        
        soma_das_nota = sum(avaliacao._nota for avaliacao in self._avaliacao)
        notas = len(self._avaliacao)
        media = round(soma_das_nota / notas,1)
        return media
        
        