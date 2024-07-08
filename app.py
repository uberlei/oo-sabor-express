from modelos.restaurante import Restaurante

restaurante = Restaurante('teste 1','Cat Teste 1')
restaurante.receber_avaliacao("Cli 1",10)
restaurante.receber_avaliacao("Cli 2",8)
restaurante.receber_avaliacao("Cli 3",5)
restaurante.receber_avaliacao("Cli 4",3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()