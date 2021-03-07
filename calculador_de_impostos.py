from impostos import ICMS, ISS, ICPP, IKCV

class Calculador_de_impostos(object):
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)

if __name__ == '__main__':
    from orcamento import Orcamento, Item

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item 1', 50))
    orcamento.adiciona_item(Item('Item 2', 200))
    orcamento.adiciona_item(Item('Item 3', 250))

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())