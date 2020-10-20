# importando bibliotecas necessárias para a execução do código
import sys

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def acc(*args):
    return np.sum(args)


def avaliar_covid(in_met_defuzz,
                  in_tosse, in_febre, in_coriza, in_dorGarganta,
                  in_dificuldadeRespirar, in_anosmia, in_disturbiosGastrintestinais,
                  in_astenia, in_hiporexia, in_dispneia, in_print_state=False):
    # Definição
    # Tosse
    # Febre
    # Coriza
    # Dor de garganta
    # Dificuldade para respirar
    # Perda de olfato (anosmia)
    # Alteração do paladar (ageusia)
    # Distúrbios gastrintestinais (náuseas/vômitos/diarreia)
    # Cansaço (astenia)
    # Diminuição do apetite (hiporexia)
    # Dispnéia ( falta de ar)

    # Antecedentes
    tosse = ctrl.Antecedent(np.arange(0, 100, 0.1), 'tosse')
    febre = ctrl.Antecedent(np.arange(0, 100, 0.1), 'febre')
    coriza = ctrl.Antecedent(np.arange(0, 100, 0.1), 'coriza')
    dorGargante = ctrl.Antecedent(np.arange(0, 100, 0.1), 'dorGarganta')
    dificuldadeRespirar = ctrl.Antecedent(np.arange(0, 100, 0.1), 'dificuldadeRespirar')
    anosmia = ctrl.Antecedent(np.arange(0, 100, 0.1), 'anosmia')
    disturbiosGastrintestinais = ctrl.Antecedent(np.arange(0, 100, 0.1), 'disturbiosGastrintestinais')
    astenia = ctrl.Antecedent(np.arange(0, 100, 0.1), 'astenia')
    hiporexia = ctrl.Antecedent(np.arange(0, 100, 0.1), 'hiporexia')
    dispneia = ctrl.Antecedent(np.arange(0, 100, 0.1), 'dispneia')

    # Consequentes

    # Chance de estar com covid19
    chanceEstarContaminado = ctrl.Consequent(np.arange(0, 100, 0.1), 'chanceEstarContaminado',
                                             defuzzify_method=in_met_defuzz)
    chanceEstarContaminado.accumulation_method = acc

    # Entradas
    # Tosse
    tosse['baixa'] = fuzz.trimf(tosse.universe, [0, 0, 35])
    tosse['media'] = fuzz.trimf(tosse.universe, [20, 45, 85])
    tosse['alta'] = fuzz.trimf(tosse.universe, [70, 100, 100])

    # Febre
    febre['baixa'] = fuzz.trimf(febre.universe, [0, 0, 35])
    febre['media'] = fuzz.trimf(febre.universe, [20, 45, 85])
    febre['alta'] = fuzz.trimf(febre.universe, [70, 100, 100])

    # Coriza
    coriza['baixa'] = fuzz.trimf(coriza.universe, [0, 0, 35])
    coriza['media'] = fuzz.trimf(coriza.universe, [20, 45, 85])
    coriza['alta'] = fuzz.trimf(coriza.universe, [70, 100, 100])

    # DorGarganta
    dorGargante['baixa'] = fuzz.trimf(dorGargante.universe, [0, 0, 35])
    dorGargante['media'] = fuzz.trimf(dorGargante.universe, [20, 45, 85])
    dorGargante['alta'] = fuzz.trimf(dorGargante.universe, [70, 100, 100])

    # DificuldadeRespirar
    dificuldadeRespirar['baixa'] = fuzz.trimf(dificuldadeRespirar.universe, [0, 0, 35])
    dificuldadeRespirar['media'] = fuzz.trimf(dificuldadeRespirar.universe, [20, 45, 85])
    dificuldadeRespirar['alta'] = fuzz.trimf(dificuldadeRespirar.universe, [70, 100, 100])

    # Anosmia
    anosmia['baixa'] = fuzz.trimf(anosmia.universe, [0, 0, 35])
    anosmia['media'] = fuzz.trimf(anosmia.universe, [20, 45, 85])
    anosmia['alta'] = fuzz.trimf(anosmia.universe, [70, 100, 100])

    # DisturbiosGastrintestinais
    disturbiosGastrintestinais['baixa'] = fuzz.trimf(disturbiosGastrintestinais.universe, [0, 0, 35])
    disturbiosGastrintestinais['media'] = fuzz.trimf(disturbiosGastrintestinais.universe, [20, 45, 85])
    disturbiosGastrintestinais['alta'] = fuzz.trimf(disturbiosGastrintestinais.universe, [70, 100, 100])

    # Astenia
    astenia['baixa'] = fuzz.trimf(astenia.universe, [0, 0, 35])
    astenia['media'] = fuzz.trimf(astenia.universe, [20, 45, 85])
    astenia['alta'] = fuzz.trimf(astenia.universe, [70, 100, 100])

    # Hiporexia
    hiporexia['baixa'] = fuzz.trimf(hiporexia.universe, [0, 0, 35])
    hiporexia['media'] = fuzz.trimf(hiporexia.universe, [20, 45, 85])
    hiporexia['alta'] = fuzz.trimf(hiporexia.universe, [70, 100, 100])

    # Dispneia
    dispneia['baixa'] = fuzz.trimf(dispneia.universe, [0, 0, 35])
    dispneia['media'] = fuzz.trimf(dispneia.universe, [20, 45, 85])
    dispneia['alta'] = fuzz.trimf(dispneia.universe, [70, 100, 100])

    # Saídas
    chanceEstarContaminado['baixa'] = fuzz.trimf(chanceEstarContaminado.universe, [0, 0, 45])
    chanceEstarContaminado['media'] = fuzz.trimf(chanceEstarContaminado.universe, [20, 45, 85])
    chanceEstarContaminado['alta'] = fuzz.trimf(chanceEstarContaminado.universe, [70, 100, 100])

    # REGRAS COVID

    # TOSSE = BAIXA , FEBRE= BAIXA, CORIZA= BAIXA, DORGARGANTA= BAIXA, DIFICULDADERESPIRAR= BAIXA, ANOSMIA=BAIXA , disturbiosGastrintestinais
    rtossebaixaum = ctrl.Rule(
        tosse['baixa'] & febre['baixa'] & coriza['baixa'] & dorGargante['baixa'] & dificuldadeRespirar['baixa'] &
        anosmia['baixa'] &
        disturbiosGastrintestinais['baixa'] & astenia['baixa'] & hiporexia['baixa'] & dispneia['baixa'],
        chanceEstarContaminado['baixa'])

    rtossebaixadois = ctrl.Rule(
        tosse['baixa'] & febre['alta'] & coriza['alta'] & dorGargante['alta'] & dificuldadeRespirar['baixa'] & anosmia[
            'baixa'] &
        disturbiosGastrintestinais['baixa'] & astenia['baixa'] & hiporexia['baixa'] & dispneia['baixa'],
        chanceEstarContaminado['alta'])

    # Completar














    chanceEstarContaminado_ctrl = ctrl.ControlSystem([rtossebaixaum, rtossebaixadois])

    # define o simulador do covid
    chanceEstarContaminado_simul = ctrl.ControlSystemSimulation(chanceEstarContaminado_ctrl)
    chanceEstarContaminado_simul.input['tosse'] = in_tosse
    chanceEstarContaminado_simul.input['febre'] = in_febre
    chanceEstarContaminado_simul.input['coriza'] = in_coriza
    chanceEstarContaminado_simul.input['dorGarganta'] = in_dorGarganta
    chanceEstarContaminado_simul.input['dificuldadeRespirar'] = in_dificuldadeRespirar
    chanceEstarContaminado_simul.input['anosmia'] = in_anosmia
    chanceEstarContaminado_simul.input['disturbiosGastrintestinais'] = in_disturbiosGastrintestinais
    chanceEstarContaminado_simul.input['astenia'] = in_astenia
    chanceEstarContaminado_simul.input['hiporexia'] = in_hiporexia
    chanceEstarContaminado_simul.input['dispneia'] = in_dispneia

    chanceEstarContaminado_simul.compute()

    if (in_print_state):
        if (sys.version_info[0] == 2):
            chanceEstarContaminado_simul.print_state()
        else:
            print('Versão do Python não compatível para impressão de sumário.')

    print(chanceEstarContaminado_simul.output['chanceEstarContaminado'])
    chanceEstarContaminado.view(sim=chanceEstarContaminado_simul)


# adicione à chamada da função as variáveis linguísticas dos antecedentes
# Os dados aqui estão sendo passados setados, será interessante, trocalos por uma interface onde pergunta os parametros
avaliar_covid('centroid', 5, 5, 4, 6, 7, 8, 9, 4, 7, 9)
