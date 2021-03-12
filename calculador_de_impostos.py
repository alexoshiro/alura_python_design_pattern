from impostos import ICMS, ISS, ICPP, IKCV

class Calculador_de_impostos(object):
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)

        return imposto_calculado

if __name__ == '__main__':
    from orcamento import Orcamento, Item

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item 1', 50))
    orcamento.adiciona_item(Item('Item 2', 200))
    orcamento.adiciona_item(Item('Item 3', 250))

    iss = calculador.realiza_calculo(orcamento, ISS())
    icms = calculador.realiza_calculo(orcamento, ICMS())
    icpp = calculador.realiza_calculo(orcamento, ICPP())
    ikcv = calculador.realiza_calculo(orcamento, IKCV())
    print('ISS', iss)
    print('ICMS', icms)
    print('ICPP', icpp)
    print('IKCV', ikcv)

    iss_com_icms = calculador.realiza_calculo(orcamento, ISS(ICMS()))
    icpp_com_ikcv = calculador.realiza_calculo(orcamento, ICPP(IKCV()))
    print('ISS COM ICMS', iss_com_icms)
    print('ICPP COM IKCV', icpp_com_ikcv)