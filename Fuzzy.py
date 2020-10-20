# importando bibliotecas necessárias para a execução do código
import sys

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


##MODELO REFERENCIA

# função para acumulação de consequentes
# por padrão, a API acumula utilizando a função MAX,
# o que altera o resultado mostrado nos slides (disponível no livro do Coppin)
def acc(*args):
    return np.sum(args)


def gestao_estoque(in_met_defuzz, in_nivel_estoque,
                   in_demanda, in_print_state=False):


    # Definição de antecedentes e consequentes
    print(plt);
    nivel_estoque = ctrl.Antecedent(np.arange(0, 100, 0.1), 'nivel_estoque')
    demanda = ctrl.Antecedent(np.arange(0, 100, 0.1), 'demanda')


    atendimento = ctrl.Consequent(np.arange(0, 100, 0.1), 'atendimento', defuzzify_method=in_met_defuzz)
    atendimento.accumulation_method = acc

    reposicao = ctrl.Consequent(np.arange(0, 100, 0.1), 'reposicao', defuzzify_method=in_met_defuzz)
    reposicao.accumulation_method = acc

    licitacao = ctrl.Consequent(np.arange(0, 100, 0.1), 'licitacao', defuzzify_method=in_met_defuzz)
    licitacao.accumulation_method = acc






    # Entradas


    # Nível Estoque
    nivel_estoque['baixa'] = fuzz.trimf(nivel_estoque.universe, [0, 0, 45])
    nivel_estoque['media'] = fuzz.trimf(nivel_estoque.universe, [30, 50, 86])
    nivel_estoque['alta'] = fuzz.trimf(nivel_estoque.universe, [70, 100, 100])


    # Demanda
    demanda['baixa'] = fuzz.trimf(nivel_estoque.universe, [0, 0, 35])
    demanda['media'] = fuzz.trimf(nivel_estoque.universe, [20, 45, 85])
    demanda['alta'] = fuzz.trimf(nivel_estoque.universe, [70, 100, 100])











    # Saídas

    # Atendimento
    atendimento['com_autorizacao'] = fuzz.trimf(nivel_estoque.universe, [0, 0, 45])
    atendimento['com_restricao'] = fuzz.trimf(nivel_estoque.universe, [20, 45, 85])
    atendimento['normal'] = fuzz.trimf(nivel_estoque.universe, [70, 100, 100])


    # Reposicao
    reposicao['baixa'] = fuzz.trimf(nivel_estoque.universe, [0, 0, 45])
    reposicao['media'] = fuzz.trimf(nivel_estoque.universe, [20, 45, 85])
    reposicao['alta'] = fuzz.trimf(nivel_estoque.universe, [70, 100, 100])

    # Licitacao
    licitacao['sim'] = fuzz.trimf(nivel_estoque.universe, [0, 0, 70])
    licitacao['nao'] = fuzz.trimf(nivel_estoque.universe, [45, 100, 100])






    # definição das regras


    #REPOSICAO

    #EstoqueBaixo
    rReposicaonivelEstoqueBaixoDemandaAlta = ctrl.Rule(nivel_estoque['baixa'] & demanda['alta'], reposicao['alta'])
    rReposicaonivelEstoqueBaixoDemandaMedia = ctrl.Rule(nivel_estoque['baixa'] & demanda['media'], reposicao['alta'])
    rReposicaonivelEstoqueBaixoDemandaBaixa = ctrl.Rule(nivel_estoque['baixa'] & demanda['baixa'], reposicao['media'])


    #EstoqueMedia
    rReposicaonivelEstoqueMediaDemandaAlta = ctrl.Rule(nivel_estoque['media'] & demanda['alta'], reposicao['alta'])
    rReposicaonivelEstoqueMediaDemandaMedia = ctrl.Rule(nivel_estoque['media'] & demanda['media'], reposicao['media'])
    rReposicaonivelEstoqueMediaDemandaBaixa = ctrl.Rule(nivel_estoque['media'] & demanda['baixa'], reposicao['baixa'])


    # EstoqueAlta
    rReposicaonivelEstoqueAltaDemandaAlta = ctrl.Rule(nivel_estoque['alta'] & demanda['alta'], reposicao['alta'])
    rReposicaonivelEstoqueAltaDemandaMedia = ctrl.Rule(nivel_estoque['alta'] & demanda['media'], reposicao['baixa'])
    rReposicaonivelEstoqueAltaDemandaBaixa = ctrl.Rule(nivel_estoque['alta'] & demanda['baixa'], reposicao['baixa'])




    # ATENDIMENTO

    # EstoqueBaixo
    rAtendimentonivelEstoqueBaixoDemandaAlta = ctrl.Rule(nivel_estoque['baixa'] & demanda['alta'], atendimento['com_autorizacao'])
    rAtendimentonivelEstoqueBaixoDemandaMedia = ctrl.Rule(nivel_estoque['baixa'] & demanda['media'], atendimento['com_restricao'])
    rAtendimentonivelEstoqueBaixoDemandaBaixa = ctrl.Rule(nivel_estoque['baixa'] & demanda['baixa'], atendimento['com_restricao'])

    # EstoqueMedia
    rAtendimentonivelEstoqueMediaDemandaAlta = ctrl.Rule(nivel_estoque['media'] & demanda['alta'], atendimento['com_restricao'])
    rAtendimentonivelEstoqueMediaDemandaMedia = ctrl.Rule(nivel_estoque['media'] & demanda['media'], atendimento['normal'])
    rAtendimentonivelEstoqueMediaDemandaBaixa = ctrl.Rule(nivel_estoque['media'] & demanda['baixa'], atendimento['normal'])

    # EstoqueAlta
    rAtendimentonivelEstoqueAltaDemandaAlta = ctrl.Rule(nivel_estoque['alta'] & demanda['alta'], atendimento['normal'])
    rAtendimentonivelEstoqueAltaDemandaMedia = ctrl.Rule(nivel_estoque['alta'] & demanda['media'], atendimento['normal'])
    rAtendimentonivelEstoqueAltaDemandaBaixa = ctrl.Rule(nivel_estoque['alta'] & demanda['baixa'], atendimento['normal'])






    # LICITACAO

    # EstoqueBaixo
    rLicitacaonivelEstoqueBaixoDemandaAlta = ctrl.Rule(nivel_estoque['baixa'] & demanda['alta'], licitacao['sim'])
    rLicitacaonivelEstoqueBaixoDemandaMedia = ctrl.Rule(nivel_estoque['baixa'] & demanda['media'], licitacao['sim'])
    rLicitacaonivelEstoqueBaixoDemandaBaixa = ctrl.Rule(nivel_estoque['baixa'] & demanda['baixa'], licitacao['nao'])

    # EstoqueMedia
    rLicitacaonivelEstoqueMediaDemandaAlta = ctrl.Rule(nivel_estoque['media'] & demanda['alta'], licitacao['sim'])
    rLicitacaonivelEstoqueMediaDemandaMedia = ctrl.Rule(nivel_estoque['media'] & demanda['media'], licitacao['nao'])
    rLicitacaonivelEstoqueMediaDemandaBaixa = ctrl.Rule(nivel_estoque['media'] & demanda['baixa'], licitacao['nao'])

    # EstoqueAlta
    rLicitacaonivelEstoqueAltaDemandaAlta = ctrl.Rule(nivel_estoque['alta'] & demanda['alta'], licitacao['nao'])
    rLicitacaonivelEstoqueAltaDemandaMedia = ctrl.Rule(nivel_estoque['alta'] & demanda['media'], licitacao['nao'])
    rLicitacaonivelEstoqueAltaDemandaBaixa = ctrl.Rule(nivel_estoque['alta'] & demanda['baixa'], licitacao['nao'])

    # define controlador do sistema
    reposicao_ctrl = ctrl.ControlSystem([rReposicaonivelEstoqueBaixoDemandaBaixa, rReposicaonivelEstoqueBaixoDemandaMedia, rReposicaonivelEstoqueBaixoDemandaAlta,
                                    rReposicaonivelEstoqueMediaDemandaBaixa,rReposicaonivelEstoqueMediaDemandaMedia,rReposicaonivelEstoqueMediaDemandaAlta,
                                    rReposicaonivelEstoqueAltaDemandaBaixa,rReposicaonivelEstoqueAltaDemandaMedia,rReposicaonivelEstoqueAltaDemandaAlta])

    atendimento_ctrl = ctrl.ControlSystem([rAtendimentonivelEstoqueBaixoDemandaBaixa, rAtendimentonivelEstoqueBaixoDemandaMedia, rAtendimentonivelEstoqueBaixoDemandaAlta,
                                    rAtendimentonivelEstoqueMediaDemandaBaixa,rAtendimentonivelEstoqueMediaDemandaMedia,rAtendimentonivelEstoqueMediaDemandaAlta,
                                    rAtendimentonivelEstoqueAltaDemandaBaixa,rAtendimentonivelEstoqueAltaDemandaMedia,rAtendimentonivelEstoqueAltaDemandaAlta])

    licitacao_ctrl = ctrl.ControlSystem([rLicitacaonivelEstoqueBaixoDemandaBaixa, rLicitacaonivelEstoqueBaixoDemandaMedia, rLicitacaonivelEstoqueBaixoDemandaAlta,
                                    rLicitacaonivelEstoqueMediaDemandaBaixa,rLicitacaonivelEstoqueMediaDemandaMedia,rLicitacaonivelEstoqueMediaDemandaAlta,
                                    rLicitacaonivelEstoqueAltaDemandaBaixa,rLicitacaonivelEstoqueAltaDemandaMedia,rLicitacaonivelEstoqueAltaDemandaAlta])



    # define o simulador de freio
    reposicao_simul = ctrl.ControlSystemSimulation(reposicao_ctrl)
    atendimento_simul = ctrl.ControlSystemSimulation(atendimento_ctrl)
    licitacao_simul = ctrl.ControlSystemSimulation(licitacao_ctrl)

    reposicao_simul.input['nivel_estoque'] = in_nivel_estoque
    reposicao_simul.input['demanda'] = in_demanda

    reposicao_simul.compute()


    atendimento_simul.input['nivel_estoque'] = in_nivel_estoque
    atendimento_simul.input['demanda'] = in_demanda

    atendimento_simul.compute()


    licitacao_simul.input['nivel_estoque'] = in_nivel_estoque
    licitacao_simul.input['demanda'] = in_demanda

    licitacao_simul.compute()








    if (in_print_state):
        if (sys.version_info[0] == 2):
            reposicao_simul.print_state()
            atendimento_simul.print_state()
            licitacao_simul.print_state()
        else:
            print('Versão do Python não compatível para impressão de sumário.')

    print(reposicao_simul.output['reposicao'])
    print(atendimento_simul.output['atendimento'])
    print(licitacao_simul.output['licitacao'])
    reposicao.view(sim=reposicao_simul)
    atendimento.view(sim=atendimento_simul)
    licitacao.view(sim=licitacao_simul)




#adicione à chamada da função as variáveis linguísticas dos antecedentes
gestao_estoque('centroid', 25, 8)